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

def my_rb(a, b): pass

def foo(sql):
    if not hasattr(my_threading_local, "a"):
        raise Exception()

    my_threading_local.a.execute(sql)

def main():
    sqlite3.sqlite3_config(191, True)
    sqlite3.sqlite3_libversion_number()

    sqlite3.sqlite3_config(SQLITE_CONFIG_URI, True)

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    sqlite3.load_extension(lib, "sqlite3_ext")

    sqlite3.sqlite3_create_function(my_threading_local.a, "test2", 2, 0, None, my_cb, None, None)

    a = sqlite3.connect(DB_URI, uri=True)
    b = sqlite3.connect(DB_URI, uri=True)

    c = sqlite3.connect(DB_URI, uri=True
