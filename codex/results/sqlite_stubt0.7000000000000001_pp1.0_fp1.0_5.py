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

so_lib = ctypes.util.find_library("sqlite3")
if not so_lib:
    raise Exception("Can't find libsqlite3")

sqlite3.sqlite_version_info

sqlite3.sqlite_version

sqlite3.sqlite_api_routines

sqlite3.threadsafety

sqlite3.paramstyle

dll = ctypes.CDLL(so_lib)

dll.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
dll.sqlite3_open_v2.restype = ctypes.c_int

dll.sqlite3_enable_load_extension.argtypes = [ctypes.c_void_p, ctypes.c_int]
dll.sqlite3_enable_load_extension.restype = ctypes.c_int

dll.sqlite3_load_extension.arg
