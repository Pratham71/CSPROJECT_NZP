import mysql.connector
import pandas 
import csv
from details import sql_details
#with mysql.connector.connect(host=hostname,user=user,passwd=password,database=database) as f:
hostname,user,password,database=sql_details()

def show_table():
    with mysql.connector.connect(host=hostname,user=user,passwd=password,database=database) as f:
        cursor=f.cursor()
        table_name="pokemon"
        query=f"select * from {table_name}"
        cursor.execute(query)
        df=pandas.read_sql_query(sql=query,con=f)
        df=df.set_index('sno')
        df=df.to_string()
        print(df)
        return

def describe_table():
    with mysql.connector.connect(host=hostname,user=user,passwd=password,database=database) as f:
        cursor=f.cursor()
        query="desc pokemon"
        cursor.execute(query)
        data=cursor.fetchall()
        header=["Field","Type","Null","Key","Default","Extra"]
        df=pandas.DataFrame(data=data,columns=header)
        print(df)
        return


def insert_table():
    with mysql.connector.connect(host=hostname,user=user,passwd=password,database=database) as f:
        cursor=f.cursor()
        desc_query="desc pokemon"
        cursor.execute(desc_query)
        desc=cursor.fetchall()
        print("Headers:")
        for x in range(len(desc)):
            print(f"{desc[x][0]}",end=",")
        print()

        new_values=[]
        for x in range(len(desc)):
            value=eval(input("enter the new values following the above format(1 by 1):"))
            new_values.append(value)
        new_values=tuple(new_values)
        print(new_values)
        query=f"insert into pokemon values{new_values}"
        cursor.execute(f"{query}")
        f.commit()

    add_more=input("add more? [y/n]:")
    if add_more.lower() in "y":
        insert_table()#recurse
    else:
        return
    return
    

def remove_table():
    with mysql.connector.connect(host=hostname,user=user,passwd=password,database=database) as f:
        cursor=f.cursor()
        query="desc pokemon"
        cursor.execute(query)
        desc=cursor.fetchall()
        print("Headers:")
        for x in range(len(desc)):
            print(f"{desc[x][0]}",end=",")
        print()
        condition_header=input("enter the condition column:")
        condition_operator=input("enter the condition operator:")
        condition=eval(input("enter the value for condition:"))

        if type(condition)==type(int()):
            query=f"delete from pokemon where {condition_header}{condition_operator}{condition}"
        elif type(condition)==type(str()):
            query=f"delete from pokemon where {condition_header}{condition_operator}'{condition}'"

        confirmation=input("are you sure you want to delete this data? [y/n]:")
        if confirmation.lower() in 'y':
            cursor.execute(query)
            f.commit()
            print("deleted the data!")
            i=input("do you want to see the table after this change? [y/n]:")
            if i.lower() in 'y':
                show_table()
                return
            else:
                print("ending the program!")
                return

            
        else:
            query=""
            print("deletion has been stopped!")
            return

def Select_table():
    with mysql.connector.connect(host=hostname,user=user,passwd=password,database=database) as f:
        cursor=f.cursor()
        
        query="desc pokemon"
        cursor.execute(query)
        desc=cursor.fetchall()
        print("Headers:")
        for x in range(len(desc)):
            print(f"{desc[x][0]}",end=",")
        print()

        condition_header=input("enter the condition column:")
        condition_operator=input("enter the condition operator:")
        condition=eval(input("enter the value for condition:"))
        print()

        query_data=[]
        while True:
            print()
            ColumnName=input("enter the column name:")
            query_data.append(ColumnName)
            Conti=input("do you want to continue? [y/n]?:")
            if Conti.lower() not in ['y']:
                break
        print()

        leng=len(query_data)
        cstring=""
        for x in range(leng):
            if x==0:
                cstring+=f"{query_data[x]}"
            else:
                cstring+=f",{query_data[x]}"

        if type(condition) == type(int()):
            qstring=f"select {cstring} from pokemon where {condition_header}{condition_operator}{condition}"
        elif type(condition) == type(str()):
            qstring=f"select {cstring} from pokemon where {condition_header}{condition_operator}'{condition}'"
        cursor.execute(qstring)
        data=cursor.fetchall()
            

        df=pandas.DataFrame(data=data,columns=query_data)
        df=df.to_string()
        print(df)
        return


def update_table():
    with mysql.connector.connect(host=hostname,user=user,passwd=password,database=database) as f:
        cursor=f.cursor()

        print("loading all the data from the sql table!\nThis may take some time!\n")
        show_table()
        print()
        query="desc pokemon"
        cursor.execute(query)
        desc=cursor.fetchall()
        print("Headers:")
        for x in range(len(desc)):
            print(f"{desc[x][0]}",end=",")
        print()
        cname=input('enter the coulmn name you want to update:')
        value=eval(input("enter the value for this column:"))
        condition_header=input("enter the condition header:")
        condition_operator=input('enter the operator:')
        condition=eval(input("enter the condition:"))
        print()
        if type(condition) == type(int()):
            query=f"update pokemon set {cname}={value} where {condition_header}{condition_operator}{condition}"
        elif type(condition)==type(str()):
            query=f"update pokemon set {cname}={value} where {condition_header}{condition_operator}'{condition}'"
        
        cursor.execute(query)
        f.commit()
        return

def alter_table():
    with mysql.connector.connect(host=hostname,user=user,passwd=password,database=database) as f:
        cursor=f.cursor()
        print("loading the field and thier constraints!\n")
        describe_table()
        print()
        options='''
~~~menu~~~
1)add column
2)drop column
3)rename column
~~~choice~~~
''' 
        print(options)
        choice=int(input("enter your choice:"))
        match choice:
            case 1:
                querys=input("enter the table name <datatype> <constraint>:")
                query="alter table ttt add {}".format(querys)
            case 2:
                querys=input("enter the table named to dropped:")
                query="alter table ttt drop {}".format(querys)
            case 3:
                before=input("enter table named to be rename:")
                after=input("enter the new name:")
                query="alter table ttt rename column {} to {}".format(before,after)
        print()
        cursor.execute(query)
        print("Altered table!")
        return

def truncate(tablename:str):
    with mysql.connector.connect(host=hostname,user=user,passwd=password,database=database) as f:
        cursor=f.cursor()
        confo=input(f"are you sure you want to truncate this table?{tablename} [y/n]:")
        if confo.lower() in 'y':
            query=f"truncate table {tablename}"
            cursor.execute(query)
            print("task completed")
            return
        return
    
def sql_to_csv(path:str):
    with mysql.connector.connect(host=hostname,user=user,passwd=password,database=database) as f:
        cursor=f.cursor()
        query="desc pokemon"
        cursor.execute(query)
        desc=cursor.fetchall()

        headers=[]
        for x in range(len(desc)):
            headers.append(desc[x][0])
        headers=tuple(headers)

        query="select * from pokemon"

        cursor.execute(query)
        data=cursor.fetchall()

        data=tuple(data)

    with open(path,"w",newline='\n') as fo:
        w=csv.writer(fo)
        w.writerow(headers)
        w.writerows(data)
        return

def csv_to_sql(path:str,tablename:str):
    """function will only work if the table is already created!
    with the macthing headers!"""
    with mysql.connector.connect(host=hostname,user=user,passwd=password,database=database) as f:
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
            query=f"select * from {tablename}"
            df=pandas.read_sql_query(query,f)
            df=df.set_index(h[0])
            df=df.to_string()
            print(df)
            return
        return
