import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.atexit(my_cb)

def test_fn(a, b):
    return a

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
conn.create_function("test", 2, test_fn)

cur = conn.cursor()
cur.execute('SELECT test(1, 2)')
assert cur.fetchall() == [(1,)]

del conn

cur = my_threading_local.a.cursor()
cur.execute('SELECT test(1, 2)')
assert cur.fetchall() == [(1,)]
