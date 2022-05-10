import threading
threading.stack_size(1024*1024*5)
import RPi.GPIO as GPIO
import time, datetime, urllib2, json, MySQLdb
import easysnmp
from time import sleep

#Init Connection Properties
hostname="bz-control-srv"
username="root"
password="123456"
database="beestat"
#hostname="localhost"
#username="root"
#password="root"
#database="bz_db"
#Connetc to Database
db = MySQLdb.connect(hostname,username,password,database)
cursor = db.cursor()
log = ""
timestamp = ""

#Global variable
global inc
#global gt
global E1_Raw
global E2_Raw
global E3_Raw
global E4_Raw
global E5_Raw
global Voltage1
global Voltage2
global Voltage3
global Voltage4
global Voltage5
global Current1
global Current2
global Current3
global Current4
global Current5
global E1_Cnt_Neg
global E2_Cnt_Neg

