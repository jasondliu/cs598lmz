import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('test.db')

# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('test.db')

def test1():
    cn = sqlite3.connect(':memory:')
    cn.execute('create table test (id integer primary key, name varchar(20))')
    cn.execute('insert into test (id, name) values (1, "abc")')
    cn.execute('insert into test (id, name) values (2, "def")')
    cn.execute('insert into test (id, name) values (3, "ghi")')
    cn.commit()
    cn.execute('select * from test')
    print(cn.fetchall())
    cn.execute('drop table test')
    cn.close()

def test2():
    print('test2')
    cn = sqlite3.connect('test.db')
    cn.execute('create table test (id integer primary key, name varchar
