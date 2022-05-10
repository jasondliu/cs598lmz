import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
try:
    con = sqlite3.connect('test.db')
    print 'sqlite3.connect() success'
except:
    print 'sqlite3.connect() failed'

# Test sqlite3.Cursor()
try:
    cur = con.cursor()
    print 'sqlite3.Cursor() success'
except:
    print 'sqlite3.Cursor() failed'

# Test sqlite3.Cursor.execute()
try:
    cur.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT, phone TEXT)')
    print 'sqlite3.Cursor.execute() success'
except:
    print 'sqlite3.Cursor.execute() failed'

# Test sqlite3.Cursor.executemany()
try:
    cur.executemany('INSERT INTO test VALUES (?, ?, ?)',
                    [
                        (1, 'John', '555-555-5555'),
                        (2, 'Jane', '555-555-5556'),
                        (3, 'Joe',
