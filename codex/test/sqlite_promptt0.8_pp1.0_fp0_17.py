import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.__init__()

def callback(ptr):
    global cb
    cb = ptr

so_name = ctypes.util.find_library('sqlite3')

if so_name is None:
    raise Exception('No sqlite3 library found')

libsqlite3 = ctypes.CDLL(so_name)

libsqlite3.sqlite3_threadsafe.restype = ctypes.c_int
threadsafety = libsqlite3.sqlite3_threadsafe()

if threadsafety == 0:
    raise Exception('sqlite3 library does not support threadsafe')

libsqlite3.sqlite3_config(ctypes.c_int(3))
db = sqlite3.connect(':memory:', check_same_thread = False)

c = db.cursor()
c.execute('create table t(x int)')

c.executemany('insert into t values (?)', [(x,) for x in range(10)])

db.create_function('callback', 1, callback)

