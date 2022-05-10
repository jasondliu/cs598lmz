import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
def test_sqlite3_connect():
    print('connect to sqlite3')
    conn = sqlite3.connect('test.db')
    print('connected')
    c = conn.cursor()
    print('cursor')
    c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
    print('create table')
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    print('insert')
    conn.commit()
    print('commit')
    c.close()
    print('close')
    conn.close()
    print('close')

# Test sqlite3.connect
def test_sqlite3_connect():
    print('connect to sqlite3')
    conn = sqlite3.connect('test.db')
    print('connected')
    c = conn.cursor()
    print('cursor')
