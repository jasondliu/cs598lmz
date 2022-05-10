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

lib = ctypes.CDLL(ctypes.util.find_library("test_sqlite"))
lib.test_sqlite_init.restype = ctypes.c_int
lib.test_sqlite_init.argtype = ctypes.c_void_p
lib.test_sqlite_init.argtypes = [ctypes.c_void_p]
lib.test_sqlite_init_safe.restype = ctypes.c_int
lib.test_sqlite_init_safe.argtype = ctypes.c_void_p
lib.test_sqlite_init_safe.argtypes = [ctypes.c_void_p]
lib.test_sqlite_deinit.restype = ctypes.c_int
lib.test_sqlite_deinit.argtype = ctypes.c_void_p
lib.test_sqlite_deinit.argtypes = [ctypes.c_void_p]
lib.test_sqlite_deinit_safe.restype = ctypes.c_int
lib.test_sqlite_deinit_
