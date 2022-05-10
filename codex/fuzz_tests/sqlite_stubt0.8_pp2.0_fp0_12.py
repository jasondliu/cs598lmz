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

libsqlite3 = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

libsqlite3.sqlite3_config(1, 1)

libsqlite3.sqlite3_initialize()

libsqlite3.sqlite3_config(1, 1)

libsqlite3.sqlite3_open.restype = ctypes.c_int
libsqlite3.sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.c_void_p]

libsqlite3.sqlite3_errcode.restype = ctypes.c_int
libsqlite3.sqlite3_errcode.argtypes = [ctypes.c_void_p]

libsqlite3.sqlite3_prepare.restype = ctypes.c_int
libsqlite3.sqlite3_prepare.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p
