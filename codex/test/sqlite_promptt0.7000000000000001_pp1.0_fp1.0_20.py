import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# Test sqlite3.connect(":memory:")

def sqlite_connect(memdb=None):
    global conn
    global cur
    if memdb is None:
        conn = sqlite3.connect('test.db')
        cur  = conn.cursor()
    else:
        conn = sqlite3.connect(':memory:')
        cur  = conn.cursor()

    return conn, cur

