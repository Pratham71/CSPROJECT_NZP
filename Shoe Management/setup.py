import mysql.connector
import pandas
import csv
from time import sleep
from details import GetDetails
host,user,passwd,database=GetDetails()

def csv_to_sql(path:str,tablename:str,database:str):
    """function will only work if the table is already created!
    with the macthing headers!"""
    with mysql.connector.connect(host=host,user=user,passwd=passwd,database=database) as f:
        with open(path,'r') as fo:
            reader=csv.reader(fo)
            reader_list=[]
            for x in reader:
                reader_list.append(tuple(x))
            h=reader_list.pop(0)
        cursor=f.cursor()
        for x in range(len(reader_list)):
            query=f"insert into {tablename} values{reader_list[x]}"
            cursor.execute(query)
        f.commit()
    
        confo=input("do you want to view the table? [y/n]:")
        if confo.lower() in 'y':
            sleep(3)
            query=f"select * from {tablename}"
            df=pandas.read_sql_query(query,f)
            df=df.set_index(h[0])
            df=df.to_string()
            print(df)
            sleep(10)
            
    return

def setup():
    try:
        with mysql.connector.connect(host=host,user=user,passwd=passwd) as f:
            cursor=f.cursor()
            query=f"create database if not exists {database}"
            cursor.execute(query)
            print("created database named {}".format(database))
            sleep(2)
            cursor.execute(f"use {database}")
            query="create table if not exists SHOES(SID int primary key,BRAND varchar(255), Name varchar(255),price int,Size varchar(10),Gender char(3),Review float)"
            cursor.execute(query)
            print("created table named shoes")
            sleep(2)
            tablename="shoes"
            path="C:\\Users\\Pratham\\Desktop\\Projetcs\\Shoe Management\\shoes.csv"
            csv_to_sql(path=path,tablename=tablename,database=database)
            print("inserted all the data into the database!")
            sleep(2)
        print("task completed!")
        sleep(1.5)
        return
    except Exception as e:
        print(e)

setup()