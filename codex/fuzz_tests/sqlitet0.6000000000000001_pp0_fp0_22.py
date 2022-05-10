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
    return 1

def my_cb3(p):
    return 1

def my_cb4(p):
    return 1

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
lib.sqlite3_enable_load_extension(None, 1)
lib.sqlite3_open(":memory:", ctypes.byref(my_threading_local.db))
lib.sqlite3_create_function(my_threading_local.db, "my_cb", 0, None, my_cb, None, None)
lib.sqlite3_create_function(my_threading_local.db, "my_cb2", 0, None, my_cb2, None, None)
lib.sqlite3_create_function(my_threading_local.db, "my_cb3", 0, None, my_cb3, None, None)
lib.sqlite3_create_function(my_threading_local.db, "my_cb4", 0,
