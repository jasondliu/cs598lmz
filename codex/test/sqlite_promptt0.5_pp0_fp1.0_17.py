import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect('example.db')

# Test sqlite3.Cursor
cur = conn.cursor()

# Test sqlite3.Cursor.execute
cur.execute('create table if not exists stocks (date text, trans text, symbol text, qty real, price real)')

# Test sqlite3.Cursor.executemany
cur.executemany('insert into stocks values (?,?,?,?,?)', [
    ('2006-01-05','BUY','RHAT',100,35.14),
    ('2006-03-28','BUY','IBM',1000,45.00),
    ('2006-04-05','SELL','IBM',500,53.00),
])

# Test sqlite3.Cursor.execute
t = ('RHAT',)
cur.execute('select * from stocks where symbol=?', t)

# Test sqlite3.Cursor.fetchall
