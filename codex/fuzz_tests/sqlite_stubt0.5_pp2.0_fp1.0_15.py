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

def my_cb2(p):
    my_threading_local.a.close()
    return 1

def my_cb3(p):
    my_threading_local.a.close()
    return 1

def my_cb4(p):
    my_threading_local.a.close()
    return 1

def my_cb5(p):
    my_threading_local.a.close()
    return 1

def main():
    p = ctypes.c_void_p()
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open(":memory:", ctypes.byref(p))
    lib.sqlite3_create_function(p, "my_cb", 0, 0, None, my_cb, None, None)
    lib.sqlite3_create_function(p, "my_cb2", 0, 0, None, my_cb2, None, None)
    lib.sqlite3_create_function(p, "my
