import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('test.db')
# print "Opened database successfully";
# conn.close()

# Test sqlite3.Cursor.execute
# conn = sqlite3.connect('test.db')
# print "Opened database successfully";
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
# print "Table created successfully";
# conn.close()

# Test sqlite3.Cursor.executemany
# conn = sqlite3.connect('test.db')
# print "Opened database successfully";
# cursor = conn.cursor()
# cursor.executemany("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (:id,:name,:age,:address,:salary)",
