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

sqlite3.sqlite3_open_v2 = sqlite3.sqlite_version_info[0] >= 3 and sqlite3.sqlite_version_info[1] >= 7 and hasattr(sqlite3, "sqlite3_open_v2")

if sqlite3.sqlite3_open_v2:
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True)
    open_v2 = lib.sqlite3_open_v2
    open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p),
                        ctypes.c_int, ctypes.c_char_p]
    open_v2.restype = ctypes.c_int

