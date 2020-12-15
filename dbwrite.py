import sys
import logging
import pymysql
import os
import pyodbc
from ast import literal_eval

#rds settings
server  = os.environ['db_url']
username = os.environ['db_user']
password = os.environ['db_password']
database = os.environ['db_name']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


#conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

logger.info("SUCCESS: Connection to RDS instance succeeded")

cursor = cnxn.cursor()


def write_to_db(firstname,lastname):
    with cnxn.cursor() as cursor:
        #cur.execute("create table IF NOT EXISTS applicationdata (ID int AUTO_INCREMENT NOT NULL, firstname varchar(255), lastname varchar(255), PRIMARY KEY (ID));")
        #cur.execute('insert into applicationdata (firstname,lastname) values(%s,%s)',(firstname,lastname))
        cursor.execute("""INSERT INTO applicationdata (firstname,lastname) VALUES ('{firstname}', '{lastname}')""")
        cnxn.commit()
    cnxn.commit()

    return "Added data to RDS table"
