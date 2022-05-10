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

def my_cb2(a, b):
    return 1

def my_cb3(a, b):
    return 1

def my_cb4(a, b):
    return 1

def my_cb5(a, b):
    return 1

def my_cb6(a, b):
    return 1

def my_cb7(a, b):
    return 1

def my_cb8(a, b):
    return 1

def my_cb9(a, b):
    return 1

def my_cb10(a, b):
    return 1

def my_cb11(a, b):
    return 1

def my_cb12(a, b):
    return 1

def my_cb13(a, b):
    return 1

def my_cb14(a, b):
    return 1

def my_cb15(a, b):
    return 1

def my_cb16(a, b):
    return 1

def my_cb17(a, b):
    return
