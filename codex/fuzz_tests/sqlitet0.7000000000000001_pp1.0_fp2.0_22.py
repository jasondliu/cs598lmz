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

def my_cb2(a, b, c):
    return 1

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.atexit(my_cb)
libc.atexit(my_cb2)

def test_fn(a, b):
    return a

def test_fn2(a, b, c):
    return a

def test_fn3(a, b, c, d):
    return a

def test_fn4(a, b, c, d, e):
    return a

def test_fn5(a, b, c, d, e, f):
    return a

def test_fn6(a, b, c, d, e, f, g):
    return a

def test_fn7(a, b, c, d, e, f, g, h):
    return a

def test_fn8(a, b, c, d, e, f, g, h, i):
    return a

def test_fn9(a
