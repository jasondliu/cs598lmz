import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

# Create table
def create_table():
    conn = sqlite3.connect('test.db')
    print "Opened database successfully"
    c = conn.cursor()
    c.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
    print "Table created successfully"
    conn.commit()
    conn.close()

# Insert data
def insert_data():
    conn = sqlite3.connect('test.db')
    print "Opened database successfully"
    c = conn.cursor()
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00 )");
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Allen',
