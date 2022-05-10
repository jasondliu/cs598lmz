import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Test sqlite3.connect()

def connect(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    conn.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
