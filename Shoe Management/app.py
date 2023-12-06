import mysql.connector
from details import GetDetails
from time import sleep
host,user,passwd,database=GetDetails()

def AddItem():
    with mysql.connector.connect(host=host,user=user,passwd=passwd,database=database) as con:
        cursor=con.cursor()

        ans="y"
        while ans.lower() in "y":
            print()
            SID=int(input("Enter the id of the shoe:"))
            Brand=input("Enter the brand for the shoe:")
            Name=input("Enter the name of shoe:")
            Size=input("Enter the size of shoe:")
            Gender=input("Enter the gender for the shoe [M/F or U for Unisex]:")
            Rating=float(input("Enter the rating for the shoe:"))

            try:
                query=f"insert into shoes values({SID},'{Brand}','{Name}','{Size}','{Gender}',{Rating})"
                cursor.execute(query)
                con.commit()
                print("inserted the details of the shoes!")
            except Exception as e:
                print(e)
                break
        
            print()
            ans=input("Do you want to add more shoes [y/n]:")

def UpdateItem():
    with mysql.connector.connect(host=host,user=user,passwd=passwd,database=database) as con:
        cursor=con.cursor()

        query="desc shoes"
        cursor.execute(query)
        headers=[i[0] for i in cursor.fetchall()]
        ans="y"
        while ans.lower() in "y":
            SID=int(input("Enter the shoe id:"))
            query=f"select * from shoes where sid={SID}"
            cursor.execute(query)
            data=cursor.fetchone()
            print(f"{data}\n")

            print("\n~~~Update Menu~~~")
            print(f"1){headers[1]}")
            print(f"2){headers[2]}")
            print(f"3){headers[3]}")
            print(f"4){headers[4]}")
            print("5)Rating")
            choice=int(input("Enter your choice:"))
            print("\n")
            if choice == 1:
                new_brand=input("Enter the new brand for this shoe:")
                query=f"Update shoes set brand='{new_brand}' where sid={SID}"
                cursor.execute(query)
                con.commit()
            
            elif choice == 2:
                new_name=input("Enter the new name of shoe:")
                query=f"Update shoes set name='{new_name}' where sid={SID}"
                cursor.execute(query)
                con.commit()

            elif choice == 3:
                new_size=input("Enter the size of shoe [foramt: USX or UKX x being a number]:")
                query=f"Update shoes set size='{new_size}' where sid={SID}"
                cursor.execute(query)
                con.commit()

            
            elif choice == 4:
                new_gender=input("Enter the new gender for the shoe [M/F or U for Unisex]:")
                query=f"update shoes set gender='{new_gender}' where sid = {SID}"
                cursor.execute(query)
                con.commit()

            
            elif choice == 5:
                new_review=float("Enter the new rating for the shoe:")
                query=f"update shoes set review='{new_review}' where sid = {SID}"
                cursor.execute(query)
                con.commit()
            else:
                print("Invalid Choice!")
            ans=input("Do you want to use more operations? [y/n]:")
           
def ShowItems():
    with mysql.connector.connect(host=host,user=user,passwd=passwd,database=database) as con:
        cursor=con.cursor()
        query=f"desc shoes"
        cursor.execute(query)
        data=cursor.fetchall()
        headers=[i[0] for i in data]
        print(headers)
        
        query="select * from shoes"
        cursor.execute(query)
        data=cursor.fetchall()

        for x in data:
            print(list(x))

def RemoveItem():
    with mysql.connector.connect(host=host,user=user,passwd=passwd,database=database) as con:
        cursor=con.cursor()
        SID=input("Enter the shoe id that has to be deleted:")
        ans=input("Are you sure you want to delete this record[y/n]:")
        ans="y"
        if ans.lower() in "y":
            try:
                query=f"delete from shoes where sid={SID}"
                cursor.execute(query)
                print(f"Deleted shoe id: {SID}.")
            except Exception as e:
                print("shoe does not exist in the database.")
            else:
                con.commit()
    return

def ClearTable():
    with mysql.connector.connect(host=host,user=user,passwd=passwd,database=database) as con:
        cursor=con.cursor()
        ans=input("Are you sure you want to clear the table[y/n]:")
        if ans.lower() in "y":
            ans=input("Are you sure you want to clear the whole table this process is not reversible [y/n:]")
            if ans.lower() in "y":
                print("Clearing the table contents in...")
                sleep(0.3)
                print(5)
                sleep(0.3)
                print(4)
                sleep(0.3)
                print(3)
                sleep(0.3)
                print(2)
                sleep(0.3)
                print(1)
                sleep(0.3)
                query="Truncate shoes"
                cursor.execute(query)
                print("Table has been cleared!")
    return

def main():
    while True:
        print("\n~~~~Menu~~~~")
        print("1)Add Item into table")
        print("2)Show Table")
        print("3)Update Items")
        print("4)Remove Items")
        print("5)Clear Table")
        print("6)Exit")


        choice = int(input("Enter your choice:"))

        if choice == 1:
            AddItem()
        elif choice == 2:
            ShowItems()
        elif choice == 3:
            UpdateItem()
        elif choice == 4:
            RemoveItem()
        elif choice == 5:
            ClearTable()
        elif choice == 6:
            print("Ending Program")
            break
        else:
            print("Invalid Choice/nTry Again")
main()
