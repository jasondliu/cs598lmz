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

def f():
    sqlite3.connect(DB_URI, uri=True)
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_function("test", 2, lambda a,b: a)
    my_threading_local.conn = conn

def g():
    conn = my_threading_local.conn
    conn.execute("select test(1, 2)")

def test_fn(a, b):
    return a

def thread_function():
    sqlite3.connect(DB_URI, uri=True)
    my_threading_local.conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.conn.create_function("test", 2, test_fn)
    test(my_threading_local.conn)

def test(conn):
    conn.execute("select test(1, 2)")

def load_library_from_path(path):

