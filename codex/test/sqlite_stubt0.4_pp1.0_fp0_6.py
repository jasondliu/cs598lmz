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

def my_cb_2(p):
    a = my_threading_local.a
    a.close()
    return 1

def my_cb_3(p):
    return 1

def my_cb_4(p):
    return 1

def my_cb_5(p):
    return 1

def my_cb_6(p):
    return 1

def my_cb_7(p):
    return 1

def my_cb_8(p):
    return 1

def my_cb_9(p):
    return 1

def my_cb_10(p):
    return 1

def my_cb_11(p):
    return 1

def my_cb_12(p):
    return 1

def my_cb_13(p):
    return 1

def my_cb_14(p):
    return 1

def my_cb_15(p):
    return 1

def my_cb_16(p):
    return 1

