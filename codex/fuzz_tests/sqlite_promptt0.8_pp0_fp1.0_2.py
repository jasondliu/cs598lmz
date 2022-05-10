import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
DB_STRING = "test.db"
conn = sqlite3.connect(DB_STRING)

def create_table():
    c = conn.cursor()
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')
    conn.commit()
    c.close()

def input_data():
    c = conn.cursor()
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    conn.commit()
    c.close()

def input_many():
    c = conn.cursor()
    purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                 ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                 ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                 ]
    c.executemany('INSERT INTO stocks VALUES (?,?,?,
