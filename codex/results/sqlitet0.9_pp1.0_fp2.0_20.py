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


ocall_sqlite3_open = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open
ocall_sqlite3_open.argtypes = [c_char_p, c_void_p]
ocall_sqlite3_open.restype = c_int
ocall_sqlite3_open_v2 = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open_v2
ocall_sqlite3_open_v2.argtypes = [c_char_p, c_void_p, c_int, c_char_p]
ocall_sqlite3_open_v2.restype = c_int
ocall_sqlite3_key = ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_key
ocall_sqlite3_key.argtypes = [c_void_p, c_char_p, c_int]
ocall_sqlite3_key.restype =
