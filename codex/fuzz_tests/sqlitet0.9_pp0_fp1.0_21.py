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

def main():
    py_path = ctypes.util.find_library('sqlite3')
    libsql = ctypes.CDLL(py_path)

    f = libsql.sqlite3_initialize
    f.argtypes = []
    f.restype = libsql.SQLITE_OK
    f()

    f = libsql.sqlite3_open_v2
    f.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
    f.restype = libsql.SQLITE_OK
    db_ptr = ctypes.c_void_p(None);
    f(DB_URI, ctypes.byref(db_ptr), 2, None);
    db = ctypes.cast(db_ptr, ctypes.POINTER(ctypes.c_void_p))

    f = libsql.sqlite3_config
    f.argtypes = [ctypes.c_int, ctypes.c_void
