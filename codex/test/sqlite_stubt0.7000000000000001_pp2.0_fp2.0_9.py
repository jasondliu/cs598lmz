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

def my_cb_deinit(p):
    my_threading_local.a.close()
    return 0

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(ctypes.c_void_p()))
lib.sqlite3_initialize()
#lib.sqlite3_config(lib.SQLITE_CONFIG_URI, 1)
lib.sqlite3_config(lib.SQLITE_CONFIG_SINGLETHREAD)
lib.sqlite3_config(lib.SQLITE_CONFIG_MULTITHREAD)
lib.sqlite3_config(lib.SQLITE_CONFIG_SERIALIZED)
#lib.sqlite3_config(lib.SQLITE_CONFIG_MUTEX, ctypes.c_void_p(0x12345678))
lib.sqlite3_config(lib.SQLITE_CONFIG_MEMSTATUS, 0)
lib.sqlite3_
