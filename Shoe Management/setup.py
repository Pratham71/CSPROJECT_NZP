import mysql.connector
from details import GetDetails
host,user,passwd,database=GetDetails()
def setup():
    try:
        with mysql.connector.connect(host=host,user=user,passwd=passwd) as f:
            cursor=f.cursor()
            query=f"create database if not exists {database}"
            cursor.execute(query)
            query=f"use {database}"
            cursor.execute(query)
            query="create table if not exists SHOES(SID int primary key,BRAND varchar(255), Name varchar(255),Size varchar(10),Gender char(3),Review int)"
            cursor.execute(query)
            print('Completed')
        return
    except Exception as e:
        print(e)

setup()