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
    my_threading_local.a.close()
    return 1

def my_cb3(p):
    return 1

def my_cb4(p):
    return 1

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_config(ctypes.c_int(lib.SQLITE_CONFIG_MULTITHREAD))

lib.sqlite3_config(ctypes.c_int(lib.SQLITE_CONFIG_URI), ctypes.c_int(1))

lib.sqlite3_initialize()

lib.sqlite3_open_v2("file:test?mode=memory", ctypes.c_void_p(0), ctypes.c_int(lib.SQLITE_OPEN_READWRITE | lib.SQLITE_OPEN_CREATE | lib.SQLITE_OPEN_URI), None)

lib.sqlite3_shutdown()

lib.sqlite3_initialize()

lib.
