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

def test_fn(a, b):
    return a

def test_factory():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_function("test", 2, test_fn)
    return conn

def test_factory_with_threading():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_function("test", 2, test_fn)
    my_threading_local.a = conn
    return conn

def test_factory_with_threading_and_cb():
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.create_function("test", 2, test_fn)
    my_threading_local.a = conn
    return conn

def test_factory_with_threading_and_cb_and_threading_local():
    conn = sqlite3.connect(DB_URI
