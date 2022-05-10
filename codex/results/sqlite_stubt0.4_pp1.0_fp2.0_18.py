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
    a.close()
    return 1

def my_cb3(p):
    a = my_threading_local.a
    a.close()
    return 1

sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.a))

sqlite3.sqlite3_create_function(my_threading_local.a, b"test", 2,
                                sqlite3.SQLITE_UTF8, None, my_cb, None, None)

sqlite3.sqlite3_create_function(my_threading_local.a, b"test2", 2,
                                sqlite3.SQLITE_UTF8, None, my_cb2, None, None)

sqlite3.sqlite3_create_function(my_threading_local.a, b"test3", 2,
                                sqlite3.SQLITE_UTF8, None, my_cb3, None, None)
