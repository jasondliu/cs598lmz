import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# c.execute('create table if not exists test (id integer primary key, name varchar(10))')
# c.execute('insert into test (name) values (?)', ('test',))
# conn.commit()
# c.execute('select * from test')
# print(c.fetchall())
# conn.close()

# Test sqlite3.connect with memory
# conn = sqlite3.connect(':memory:')
# c = conn.cursor()
# c.execute('create table if not exists test (id integer primary key, name varchar(10))')
# c.execute('insert into test (name) values (?)', ('test',))
# conn.commit()
# c.execute('select * from test')
# print(c.fetchall())
# conn.close()

# Test sqlite3.connect with memory and thread
# def test():
#     conn = sqlite3.connect(':memory:')
#     c = conn.
