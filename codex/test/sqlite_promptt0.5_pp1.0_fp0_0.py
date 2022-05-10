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
