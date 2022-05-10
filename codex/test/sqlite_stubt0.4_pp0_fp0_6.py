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
    a = my_threading_local.a
    a.execute("select test(1, 2)")
    return 1

def main():
    lib = ctypes.util.find_library("sqlite3")
    sqlite3 = ctypes.CDLL(lib)

    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)
    sqlite3.sqlite3_initialize()

    sqlite3.sqlite3_create_function(None, "my_cb", 1, sqlite3.SQLITE_UTF8, None, my_cb)
    sqlite3.sqlite3_create_function(None, "my_cb2", 1, sqlite3.SQLITE_UTF8, None, my_cb2)

