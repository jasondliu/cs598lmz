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

def test_functools_partial():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.enable_load_extension(1)
    a.load_extension(ctypes.util.find_library("sqlite3"))
    a.create_function("my_cb", 0, functools.partial(my_cb))
    a.create_function("my_cb2", 0, functools.partial(my_cb2))
    a.execute("select my_cb()")
    a.execute("select my_cb2()")

def test_create_function():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.enable_load_extension(1)
    a.load_extension(ctypes.util.find_library("sqlite3"))
    a.create_function("my
