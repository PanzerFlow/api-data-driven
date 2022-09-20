from os import listdir
from os.path import isfile, join
import config # importing `config.py` to access its variables
import pandas as pd
import sqlalchemy

database_username = config.api_global_temp_user
database_password = config.api_global_temp_password
database_Endpoint = config.api_global_temp_host
database_name     = config.api_global_temp_db
database_engine = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_Endpoint, database_name))

file = R'./data/20100001.csv'
df_master = pd.read_csv(file)
#print(df_master.head(5).to_string())
df_master.to_sql(con=database_engine, name='tester2', if_exists='replace')
