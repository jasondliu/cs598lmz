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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)

def test_fn(a, b):
    return a

def test_fn2(a, b):
    return a

def test_fn3(a, b):
    return a

def test_fn4(a, b):
    return a

def test_fn5(a, b):
    return a

def test_fn6(a, b):
    return a

def test_fn7(a, b):
    return a

def test_fn8(a, b):
    return a

def test_fn9(a, b):
    return a

def test_fn10(a, b):
    return a

def test_fn11(a, b):
    return a

def test_fn12(a, b):
    return a

def test_fn13(a, b
