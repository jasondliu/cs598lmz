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

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(3, 1)

    lib.sqlite3_initialize()

    lib.sqlite3_create_function_v2(None, b"test", 2, 1, None, my_cb, my_cb2, my_cb3, my_cb4)

    lib.sqlite3_shutdown()

