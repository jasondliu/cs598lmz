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
    return my_threading_local.a.cursor().execute("SELECT test(?, ?)", (a, b)).fetchone()[0]

def my_cb3(p, a, b):
    return my_threading_local.a.cursor().execute("SELECT test(?, ?)", (a, b)).fetchone()[0]

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_enable_load_extension(ctypes.c_void_p(0), 1)
lib.sqlite3_load_extension(ctypes.c_void_p(0), b"test", b"test", b"test")

lib.sqlite3_create_function(ctypes.c_void_p(0), b"test", 1, 0, b"test", my_cb, None, None)
lib.sqlite3_create_function(ctypes.c_void_p(0), b"test", 2, 0
