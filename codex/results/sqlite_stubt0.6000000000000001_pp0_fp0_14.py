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

libdl = ctypes.CDLL(ctypes.util.find_library('dl'), use_errno=True)
libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

libsqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

libsqlite.sqlite3_enable_load_extension(None, 1)

libsqlite.sqlite3_open_v2(":memory:", ctypes.byref(my_threading_local.db),
                          sqlite3.SQLITE_OPEN_READWRITE |
                          sqlite3.SQLITE_OPEN_CREATE |
                          sqlite3.SQLITE_OPEN_FULLMUTEX,
                          None)

libsqlite.sqlite3_create_function(my_threading_local.db,
                                  "mycb", 1, 1, ctypes.py_object(my_cb), None, None)

libsqlite.sqlite3_exec
