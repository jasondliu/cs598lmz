import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect and sqlite3.close
SQLITE_OPEN_READONLY = 1
SQLITE_OPEN_READWRITE = 2
SQLITE_OPEN_CREATE = 4

connect = sqlite3.connect('demo.db')
connect.close()

test = sqlite3.connect('test.db', SQLITE_OPEN_READONLY, timeout=3)
test.close()

open(ctypes.util.find_library('sqlite3'), 'r').close()
# Test sqlite3.Error
import sqlite3
try:
    connect = sqlite3.connect('demo.db')
    connect.close()

except sqlite3.Error as e:
    print(e)
# Test sqlite3.DatabaseError
import sqlite3

