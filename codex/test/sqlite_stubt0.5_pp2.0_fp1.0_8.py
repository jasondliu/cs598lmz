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

def my_cb2(p, a, b):
    return my_threading_local.a.create_function("test", 2, test_fn)

def my_cb3(p, a, b):
    return my_threading_local.a.create_function("test", 2, test_fn)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(my_threading_local.a))
lib.sqlite3_create_function(my_threading_local.a, b"test", 2, None, my_cb, None, None)

# This will raise a segfault
lib.sqlite3_create_function(my_threading_local.a, b"test", 2, None, my_cb2, None, None)

# This will raise a segfault
