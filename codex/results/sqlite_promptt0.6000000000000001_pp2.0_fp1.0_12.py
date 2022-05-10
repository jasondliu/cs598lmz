import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

con = sqlite3.connect(':memory:')
print "sqlite3.connect() OK"

# Test sqlite3.Connection.execute()

cur = con.cursor()
cur.execute('create table test(id integer primary key)')
cur.execute('insert into test values(1)')
cur.execute('insert into test values(2)')
cur.execute('select * from test')
print "sqlite3.Connection.execute() OK"

# Test sqlite3.Cursor.fetchall()

print cur.fetchall()
print "sqlite3.Cursor.fetchall() OK"

# Test sqlite3.Cursor.description

print cur.description
print "sqlite3.Cursor.description OK"

# Test sqlite3.Cursor.close()

cur.close()
print "sqlite3.Cursor.close() OK"

# Test sqlite3.Connection.close()

con.close()
print "sqlite3.Connection.close() OK"

# Test sqlite3.connect
