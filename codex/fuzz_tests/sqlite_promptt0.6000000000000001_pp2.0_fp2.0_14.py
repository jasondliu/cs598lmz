import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
db=sqlite3.connect('test.db')
print "Database Created"
# Creating a cursor object using the cursor() method
cursor = db.cursor()
# create table
cursor.execute('''CREATE TABLE IF NOT EXISTS test_table
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print "Table Created"
# insert 3 rows data
cursor.execute("INSERT INTO test_table (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
cursor.execute("INSERT INTO test_table (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
cursor.execute("INSERT INTO test_table (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23,
