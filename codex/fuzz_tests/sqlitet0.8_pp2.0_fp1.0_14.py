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

def test_entry_callback():
    ctypes_sqlite_handle = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
    ctypes_sqlite_handle.sqlite3_config(ctypes_sqlite_handle.SQLITE_CONFIG_URI, 1)
    ctypes_sqlite_handle.sqlite3_config(ctypes_sqlite_handle.SQLITE_CONFIG_ENTRYPOINT_OK, 1)
    ctypes_sqlite_handle.sqlite3_config(ctypes_sqlite_handle.SQLITE_CONFIG_GETMALLOC, 0)
    ctypes_sqlite_handle.sqlite3_config(ctypes_sqlite_handle.SQLITE_CONFIG_MALLOC, 0)
    ctypes_sqlite_handle.sqlite3_config(ctypes_sqlite_handle.SQLITE_CONFIG_SINGLETHREAD)

    ctypes_sqlite_handle.sqlite3_initialize()

    ctypes_sqlite_handle.sqlite3_create_function
