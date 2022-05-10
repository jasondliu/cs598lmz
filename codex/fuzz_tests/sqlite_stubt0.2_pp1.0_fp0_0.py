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
    return 1

def my_cb4(p):
    return 1

def my_cb5(p):
    return 1

def my_cb6(p):
    return 1

def my_cb7(p):
    return 1

def my_cb8(p):
    return 1

def my_cb9(p):
    return 1

def my_cb10(p):
    return 1

def my_cb11(p):
    return 1

def my_cb12(p):
    return 1

def my_cb13(p):
    return 1

def my_cb14(p):
    return 1

def my_cb15(p):
    return 1

def my_cb16(p):
    return 1

def my_cb17(p):
    return 1

def my_cb18(p):
    return 1

def my
