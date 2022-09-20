from flask import Flask, jsonify # importing flask to construct the api
import pymysql # importing pymsql to interact with the mysql rds instance
import json # importing `config.py` to access its variables
import config # importing `config.py` to access its variables

conn = pymysql.connect(
        host= config.api_global_temp_host, 
        port = config.api_global_temp_port,
        user = config.api_global_temp_user, 
        password = config.api_global_temp_password,
        db = config.api_global_temp_db,
        )

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Flask_API_Testing</h1><p>Prototyping API.</p>"

# Average seasonal temperature for each season and year where data is available
@app.route('/tester2_sample', methods=['GET'])
def stg_seasonal_avg_temp():
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM global_temp.tester2 limit 10;")

    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    cursor.close()

    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    return json.dumps(json_data)


@app.route('/tester2_year/<string:REF_DATE>', methods=['GET'])
def with_url_variables(REF_DATE: str):
    cursor=conn.cursor()

    cursor.execute(f"SELECT * FROM global_temp.tester2 WHERE REF_DATE = '{REF_DATE}';")

    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    cursor.close()

    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    return json.dumps(json_data)

if __name__ == '__main__':
    app.run(debug=True)



"""
flask run --host=0.0.0.0 --port=8081

ctrl+z
bg
disown -h

Testing API Calls
# http://44.203.191.81:8081/
# http://44.203.191.81:8081/tester2_sample
# http://44.203.191.81:8081/tester2_year/1946-10

kill $(pgrep -f flask)
"""


