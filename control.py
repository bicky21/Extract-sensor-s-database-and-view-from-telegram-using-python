import mysql.connector
import requests   
from datetime import datetime              
import json                     
import time  
import os                 
from telegram.ext import MessageHandler, Filters  
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import re
import conf
                
print("Press 1 for shell interface")
print("Press 2 for controlling from telegram" )
op=int(input("Enter option "))
if op == 1:
    while(1):
        print("Select one of the option")
        print("\n")
        print("Press 1 for create database")
        print("Press 2 for create table")
        print("Press 3 for view table data")
        print("Press 4 for drop the database")
        print("Press 5 for show list of databases")
        print("Press 6 for drop the table")
        print("Press 7 for enter data ")
        print("Press 8 for exit ")
        choose=int(input("Choose :"))
        if choose ==1:
            db_name=input("Enter database name : ")
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="123")
            mycursor=mydb.cursor()
            mycursor.execute("CREATE DATABASE "+db_name)
            print("Database "+db_name+ "create successfully")      
        elif choose == 2:
            try:
                db_name=input("Enter database name : ")
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database=db_name)
                print("Connection Established...")
                mycursor=mydb.cursor()
                tbl=input("Enter table name : ")
                no_of_col=int(input("Enter no of column :"))
                col=input("Enter column name ")
                typ=input("Enter type ")
                rng=int(input("Enter range "))
                try:
                    mycursor.execute("CREATE TABLE "+tbl+"("+col+" "+typ+"("+str(rng)+")"+")")
                    print("Table created successfully")
                except:
                    print("Table is already exist")
            except:
                print("Database not found")
        elif choose == 3:
            try:
                db_name=input("Enter database name : ")
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database=db_name)
                print("Connection Established...")
                mycursor=mydb.cursor()
                tbl=input("Enter table name : ")
                try:
                    mycursor.execute("SELECT * from "+tbl)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        print(x)
                except:
                    print("Table is doesn't exist")
            except:
                print("Database not found")
        elif choose == 4:
            try:
                db_name=input("Enter database name : ")
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database=db_name)
                print("Connection Established...")
                mycursor=mydb.cursor()
                try:
                    mycursor.execute("DROP DATABASE "+db_name)
                    print("Database DROPPED")
                except:
                    print("Database not found")
            except:
                print("Database not found")
        elif choose == 5:
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="123")
                mycursor=mydb.cursor()
                mycursor.execute("SHOW DATABASES")
                for x in mycursor:
                   print(x)
            except:
                print("Database not found ")
        elif choose == 6:
            try:
                db_name=input("Enter database name : ")
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database=db_name)
                print("Connection Established...")
                mycursor=mydb.cursor()
                try:
                    tbl=input("Enter table to drop ")
                    mycursor.execute("DROP TABLE "+tbl)
                    print("Table DROPPED")
                except:
                    print("Table not found")
            except:
                print("Database not found")
        elif choose == 8:
            exit(1)
elif op == 2:
    
    def hello(update,context):
        message="Hi"
        context.bot.send_message(chat_id=update.effective_chat.id,text=message)
        ##############################################################################################
    def hi(update,context):
        message="WELCOME My name is Bolt sensor's Database Bot\nType /apache for start apache2 server \nType /sql for start sql server \n Type /stop_apache to stop apache2 server \n Type /stop_sql to stop sql server  \n Type /view for view sensor status from live database "
        context.bot.send_message(chat_id=update.effective_chat.id,text=message)
        ##############################################################################################
    
    def view(update,context):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="sensor")
        mycursor=mydb.cursor()
        print("Connection Established")
        mycursor.execute("SELECT * from analysis")
        myresult = mycursor.fetchall()
        msg=('\n'.join(str(e) for e in myresult))
        print("Sending...")
        context.bot.send_message(chat_id=update.effective_chat.id,text=msg)
        
            
    def apache(update,context):
        os.system("service apache2 start")
        message="Apache2 is activate,But I will send notification to my admin."
        context.bot.send_message(chat_id=update.effective_chat.id,text=message)
    def sql(update,context):
        os.system("service mysql start")
        message="SQL is activate,But I will send notification to my admin."
        context.bot.send_message(chat_id=update.effective_chat.id,text=message)
    def stop_apache(update,context):
        os.system("service apache2 stop")
        message="apache2 is deactivate,But I will send notification to my admin"
        context.bot.send_message(chat_id=update.effective_chat.id,text=message)
    def stop_sql(update,context):
        os.system("service mysql stop")
        message="SQL is deactivate,But I will send notification to my admin."
        context.bot.send_message(chat_id=update.effective_chat.id,text=message)
        ##############################################################################################

    
    updater = Updater(token='YOUR TELEGRAM TOKEN', use_context=True)
    dispatcher = updater.dispatcher
    start_handler1=CommandHandler('hello',hello)
    start_handler2=CommandHandler('hi',hi)
    start_handler5=CommandHandler('view',view)
    start_handler9=CommandHandler('apache',apache)
    start_handler10=CommandHandler('sql',sql)
    start_handler11=CommandHandler('stop_apache',stop_apache)
    start_handler12=CommandHandler('stop_sql',stop_sql)
    dispatcher.add_handler(start_handler1)
    dispatcher.add_handler(start_handler2)
    dispatcher.add_handler(start_handler5)
    dispatcher.add_handler(start_handler9)
    dispatcher.add_handler(start_handler10)
    dispatcher.add_handler(start_handler11)
    dispatcher.add_handler(start_handler12)
    updater.start_polling()
    updater.idle()
     
