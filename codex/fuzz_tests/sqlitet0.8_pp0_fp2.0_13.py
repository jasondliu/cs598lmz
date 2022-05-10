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

try:
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
except OSError:
    raise SystemError("Cannot find libsqlite3")

lib.sqlite3_initialize()

lib.sqlite3_config(
    lib.SQLITE_CONFIG_GETMUTEX,
    ctypes.pythonapi.PyThread_get_key_value.restype(ctypes.c_void_p))

lib.sqlite3_config(
    lib.SQLITE_CONFIG_MULTITHREAD)

lib.sqlite3_config(
    lib.SQLITE_CONFIG_URI, 1)

lib.sqlite3_config(
    lib.SQLITE_CONFIG_LOG, my_cb, 0)

lib.sqlite3_config(
    lib.SQLITE_CONFIG_SINGLETHREAD)

c = sqlite3.connect(DB_URI, uri=True)

def test_fn(a, b):
    return a

c.create
