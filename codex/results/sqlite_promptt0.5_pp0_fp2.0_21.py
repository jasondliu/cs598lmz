import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect, sqlite3.cursor, sqlite3.execute, sqlite3.commit, sqlite3.rollback
db = sqlite3.connect(':memory:')
cur = db.cursor()
cur.execute('create table test(id int)')
cur.execute('insert into test(id) values (?)', (1,))
db.commit()
cur.execute('select id from test')
print(cur.fetchone()[0])
cur.execute('insert into test(id) values (?)', (2,))
db.rollback()
cur.execute('select id from test')
print(cur.fetchone()[0])
# Test sqlite3.Row
cur.execute('select * from test')
row = cur.fetchone()
print(row[0])
print(row['id'])
# Test sqlite3.row_factory
db.row_factory = sqlite3.Row
cur = db.cursor()
cur.execute('select * from test')
row = cur.fetchone()
print(row[0])
print
