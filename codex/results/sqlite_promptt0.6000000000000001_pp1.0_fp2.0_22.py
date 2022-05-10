import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
db = sqlite3.connect('test')

cursor = db.cursor()
# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)

# disconnect from server
db.close()
import sqlite3

try:
   db = sqlite3.connect('test')
   cursor = db.cursor()
   cursor.execute('''CREATE TABLE employees
      (staff_number INTEGER PRIMARY KEY, fname VARCHAR(20),
       lname VARCHAR(30), gender CHAR(1), joining DATE,
       birth_date DATE)''')
   db.commit()
except:
   db.rollback()

db.close()
#
