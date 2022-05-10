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

def my_cb2():
    a = my_threading_local.a
    b = a.cursor()
    c = b.execute("select test(1, 2)")
    c.fetchone()

def f(x):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.create_function("test", 2, lambda x, y: x)
    my_threading_local.a = a
    return 1

def g():
    a = my_threading_local.a
    b = a.cursor()
    c = b.execute("select test(1, 2)")
    c.fetchone()

def test_leak_in_thread():
    libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    libsqlite3.sqlite3_thread_init()
    try:
        libsqlite3.sqlite3_create_function(None, b"test", 1, None, f
