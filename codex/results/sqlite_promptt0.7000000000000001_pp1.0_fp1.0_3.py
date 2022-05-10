import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#conn = sqlite3.connect('example.db')

# Test sqlite3.Row
#conn.row_factory = sqlite3.Row
#c = conn.cursor()
#c.execute('select * from stocks')
#r = c.fetchone()
#print(r['date'])

# Test sqlite3.version
#print('sqlite3.version = ', sqlite3.version)
#print('sqlite3.sqlite_version = ', sqlite3.sqlite_version)

# Test sqlite3.Cursor.rowcount
#print('c.rowcount = ', c.rowcount)

# Test sqlite3.Cursor.execute()
#c.execute('create table if not exists table1(id int, name text)')
#c.execute('insert into table1 values(1, \'name1\')')
#c.execute('insert into table1 values(2, \'name2\')')
#c.execute('select * from table1')
#print('c.fetchall() = ', c.f
