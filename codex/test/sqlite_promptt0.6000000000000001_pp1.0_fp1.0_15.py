import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

db_file = './test.db'

def main():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('drop table if exists stocks')
    c.execute('create table stocks (date text, trans text, symbol text, qty real, price real)')
    c.execute("insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)")
    #conn.commit()
    #conn.close()
    c.execute('select * from stocks')
