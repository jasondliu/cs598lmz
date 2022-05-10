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
    loaded_lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
except OSError:
    print("Could not find libsqlite3.so, not testing")
    raise Exception("SKIP")

loaded_lib.sqlite3_conn_status.argtypes = [ctypes.c_void_p, ctypes.c_int]
loaded_lib.sqlite3_conn_status.restype = ctypes.c_int
loaded_lib.sqlite3_db_status.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
loaded_lib.sqlite3_db_status.restype = ctypes.c_int
loaded_lib.sqlite3_status.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
loaded_lib.sqlite3_status.restype = ctypes
