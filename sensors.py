import mysql.connector
from boltiot import Bolt        
import conf 
import time
import json
import re
mybolt = Bolt(conf.bolt_api_key, conf.device_id)
while True:
        response = mybolt.serialRead('1')  
        data = json.loads(response)
        recv_data = data['value'].rstrip()
        print(recv_data)
        if((recv_data)==''):
            print("Arduino is starting")
            time.sleep(5)
        elif((recv_data)=='Command timed out'):
            print("Command Timed out")
        elif(((recv_data)=='\n') or ((recv_data)=='\r')):
            print("")
        else:
            time.sleep(5)
            x = re.findall("\D", recv_data)
            if(x):
                continue
            elif int(recv_data)<20:
                print(recv_data)
                mybolt.digitalWrite(0, 'HIGH')
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="sensor")
                mySql_insert_query = """INSERT INTO analysis (Distance_at_cm,LED_status,Connected_device) VALUES ('Less than 20 cm','1','BOLT_IOT & ARDUINO') """
                cursor = mydb.cursor()
                cursor.execute(mySql_insert_query)
                mydb.commit()
                cursor.close()
                print(cursor.rowcount, "record inserted.")
                time.sleep(5)
            elif int(recv_data)>20:
                mybolt.digitalWrite(0,'LOW')
                mydb=mysql.connector.connect(host="localhost",user="root",passwd="123",database="sensor")
                mySql_insert_query = """INSERT INTO analysis (Distance_at_cm,LED_status,Connected_device) VALUES ('Greater than 20 cm','0','BOLT_IOT & ARDUINO') """
                cursor = mydb.cursor()
                cursor.execute(mySql_insert_query)
                mydb.commit()
                cursor.close()
                print(cursor.rowcount, "record inserted.")
                time.sleep(5)
            else:
                print("Abnormal value detected")
