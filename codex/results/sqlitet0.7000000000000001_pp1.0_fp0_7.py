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

sqlite3.sqlite3_threadsafe()

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
try:
    lib.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_MULTITHREAD))
    lib.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_SERIALIZED))
except AttributeError:
    pass

sqlite3.sqlite3_initialize()
sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.h), ctypes.c_int(sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE), None)

sqlite3.sqlite3_create_function(my_threading_local.h, "test2", 2, sqlite3.SQLITE_UTF8, sqlite3.SQLITE_STATIC, my_cb, None, None)

my_
