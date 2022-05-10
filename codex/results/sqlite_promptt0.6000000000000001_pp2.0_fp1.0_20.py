import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# conn = sqlite3.connect('test.db')
# print "Opened database successfully";

# # Test sqlite3.cursor()
# cursor = conn.cursor()
# print "Cursor created successfully";

# # Test sqlite3.Cursor.execute()
# cursor.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print "Table created successfully";

# # Test sqlite3.Cursor.executemany()
# cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");
# cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15
