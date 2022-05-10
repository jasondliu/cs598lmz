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

sqlite3.sqlite3_shutdown()

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_SERIALIZED)
sqlite3.sqlite3_enable_shared_cache(True)

if sqlite3.sqlite3_initialize() != sqlite3.SQLITE_OK:
    raise Exception("Could not initialize sqlite3")

lib_handle = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

if lib_handle.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1) != sqlite3.SQLITE_OK:
    raise Exception("Could not set SQLITE_CONFIG_URI")

lib_handle.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)

lib_handle.sqlite3_config(sqlite3.SQLITE_CONFIG_GETMALLOC, ctypes.pointer(ctypes.c_void_p()))
lib_handle.sqlite3_config(sqlite3
