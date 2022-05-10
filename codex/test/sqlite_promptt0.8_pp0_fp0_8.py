import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# conn = sqlite3.connect('test.db')
# conn.execute('''CREATE TABLE TESTDATA
#     (ID INT PRIMARY KEY     NOT NULL,
#     DATETIME           DATE    NOT NULL,
#     PRESSURE           REAL    NOT NULL,
#     HUMIDITY           REAL    NOT NULL,
#     TEMPERATURE           REAL    NOT NULL);''')

# Test sqlite3.connect()
conn = sqlite3.connect('test.db')
c = conn.cursor()

# c.execute("""DROP TABLE TESTDATA;""")
c.execute('''CREATE TABLE TESTDATA
    (ID INT PRIMARY KEY     NOT NULL,
    DATETIME           DATE    NOT NULL,
    PRESSURE           REAL    NOT NULL,
    HUMIDITY           REAL    NOT NULL,
    TEMPERATURE           REAL    NOT NULL);''')

ID = '2'
DATETIME = '2016-12-14 18:32:11'
PRESSURE = '1020.5'
