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

def my_cb_no_conn(p):
    return 1

def my_cb_open_conn(p):
    my_threading_local.a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    return 1

def my_cb_open_conn_unmanaged(p):
    my_threading_local.a = sqlite3.connect(DB_URI, uri=True)
    return 1

def my_cb_open_conn_gc(p):
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn = None

    return 1

def my_cb_one_open_conn(p):
    my_threading_local.a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    return 0

def test_callback():
    lib = ctypes.util.find_library('sqlite3')
    if not lib:
        raise AssertionError
