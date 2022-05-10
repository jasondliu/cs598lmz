import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('create table test(id integer, name varchar(255));')
cur.execute('insert into test (id, name) values (?, ?)', (1, 'test'))
conn.commit()
cur.execute('select * from test;')
