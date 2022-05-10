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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_config(lib.SQLITE_CONFIG_URI, 1)
lib.sqlite3_config(lib.SQLITE_CONFIG_SINGLETHREAD)

lib.sqlite3_enable_shared_cache(1)

lib.sqlite3_open_v2(b":memory:", ctypes.byref(ctypes.c_void_p()), lib.SQLITE_OPEN_READWRITE | lib.SQLITE_OPEN_CREATE | lib.SQLITE_OPEN_URI, None)

lib.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(ctypes.c_void_p()), lib.SQLITE_OPEN_READWRITE | lib.SQLITE_OPEN_CREATE | lib.SQLITE_OPEN_URI, None)

lib.sqlite3_open_v2(DB_URI.encode(), ctypes.byref(ctypes.c_
