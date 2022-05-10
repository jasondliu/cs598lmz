import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect('test.db')
# Get a cursor object
cursor = conn.cursor()
cursor.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, 
             qty real, price real)''')
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
t = ('RHAT',)
cursor.execute('SELECT * FROM stocks WHERE symbol=?', t)
