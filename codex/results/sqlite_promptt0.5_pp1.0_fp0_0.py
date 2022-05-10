import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# connect = sqlite3.connect('test.db')
# print "Opened database successfully";
# cursor = connect.cursor()
# cursor.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
# print "Table created successfully";
# connect.commit()
# connect.close()

def test():
    connect = sqlite3.connect('test.db')
    print "Opened database successfully";
    cursor = connect.cursor()
    cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");


