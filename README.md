# api-data-driven

- api-data-driven (Python, Flask, Mysql)
  - [1. Introduction](#1-introduction)
  - [2. Design](#2-design)
  - [3. Output](#3-output)
  - [4. Setup](#4-setup)

## 1. Introduction
The goal of this project is to build a simple data driven api that can serve data to external users. 
The final output of this project is an simple api that have two end points which allow user to extract data. 

This project is used as an learning opportunity for me to develop skills and experience.
As such, the project is simpler than it reuqired in production. 



## 2. Design


## 3. Output


## 4. Setup
Prerequisites
    1. EC2 instance
    2. MYSQL RDS instance (In the same VPC as EC2)
    3. Git

In you EC2 instance, use git to clone this repo
```bash
git clone https://github.com/PanzerFlow/api-data-driven.git
```

Create python virtual environment used for this project
```bash
python3 -m venv venv
source venv/bin/activate
pip install sqlalchemy pandas mysql-connector
```

Create the config file to store your MYSQL RDS secerts. 
Update the string with your own MYSQL RDS secerts.
```bash
touch config.py

echo "api_global_temp_host = 'replace with your own config'" >> config.py
echo "api_global_temp_port = 'replace with your own config'" >> config.py
echo "api_global_temp_user = 'replace with your own config'" >> config.py
echo "api_global_temp_password = 'replace with your own config'" >> config.py
echo "api_global_temp_db = 'replace with your own config'" >> config.py
```

Run the data import script using the activated python virtual environment
```bash
python import_data.py
```
