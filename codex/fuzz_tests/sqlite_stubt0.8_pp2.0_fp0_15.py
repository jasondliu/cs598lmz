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

def get_conn():
    try:
        a = my_threading_local.a
    except AttributeError:
        return sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    else:
        return a

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    cb_func = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)
    lib.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
    lib.sqlite3_open_v2.restype = ctypes.c_int
    lib.sqlite3_open_v2(
        b"test",
        ctypes.byref(ctypes.c_void_p()),
        0x00000008,  # SQLITE_OPEN_URI
        ctypes
