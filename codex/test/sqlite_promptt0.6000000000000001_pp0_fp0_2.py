import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() success
def connect_db():
    db = sqlite3.connect('test.db')
    print("Opened database successfully")
    db.close()

# Test sqlite3.connect() fail
def connect_db_fail():
    db = sqlite3.connect('test_none.db')
    print("Opened database successfully")
    db.close()

# Test sqlite3.connect() success
def connect_db2():
    db = sqlite3.connect('test1.db')
    print("Opened database successfully")
    db.close()

# Test sqlite3.connect() fail
def connect_db2_fail():
    db = sqlite3.connect('test1_none.db')
    print("Opened database successfully")
    db.close()

# Test sqlite3.connect() success
def connect_db3():
    db = sqlite3.connect('test2.db')
    print("Opened database successfully")
    db.close()

# Test sqlite3.connect() fail
