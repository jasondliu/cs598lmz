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

def my_cb_final(p):
    my_threading_local.a.close()
    my_threading_local.a = None

    return 1

libsqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

libsqlite.sqlite3_initialize()

libsqlite.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))

libsqlite.sqlite3_config(ctypes.c_int(3), ctypes.c_int(1))

libsqlite.sqlite3_config(ctypes.c_int(7), ctypes.c_void_p(my_cb))

libsqlite.sqlite3_config(ctypes.c_int(8), ctypes.c_void_p(my_cb_final))

def test_create_function():
    a = sqlite3.connect(DB_URI, uri=True)

    def test_fn(a, b):
        return a

    a.
