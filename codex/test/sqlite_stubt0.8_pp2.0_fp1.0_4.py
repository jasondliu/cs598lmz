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

def test_func(a, b):
    return a

SQL = "SELECT test(1,2);"

libsqlite3 = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))

libsqlite3.sqlite3_open_v2(DB_URI.encode('ascii'), ctypes.byref(my_threading_local.db), 0x00000008 | 0x00000020, None)

