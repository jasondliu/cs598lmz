import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Prepare a sample database

con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('create table test(id)')

cur.execute('insert into test values (1)')
cur.execute('insert into test values (2)')
cur.execute('insert into test values (3)')

cur.execute('select id from test')
print(cur.fetchall())

# Test sqlite3.connect()

import sqlite3

conn = sqlite3.connect(':memory:')

cursor = conn.cursor()

cursor.execute('create table person(id integer primary key,name varchar(20))')
cursor.execute('insert into person values(1,"Michael")')

conn.commit()

cursor.close()

cursor = conn.cursor()
cursor.execute('select * from person where id=1')
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()

# Test sqlite3.register
