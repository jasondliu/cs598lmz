import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")
# Create table import ctypes
import ctypes.util
import threading
import sqlite3
conn.execute('''CREATE TABLE COMPANY
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("Table created successfully");
# Make a db file and an empty table in the db file
conn = sqlite3.connect('test.db')
# Table 1
conn.execute('''CREATE TABLE COMPANY
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("Table created successfully");

# Table 2
conn.execute('''CREATE TABLE STUDENT
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("Table created successfully");

conn.close()
# Insert data into the table
