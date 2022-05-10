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

def get_ptr(atom):
    if not hasattr(atom, "__pointer__"):
        raise TypeError(atom)
    return atom.__pointer__()

CFUNCTYPE = ctypes.CFUNCTYPE

def sqlite3_open_ptr(uri):
    sqlite3_open_ptr = ctypes.c_void_p.in_dll(
        sqlite3, "sqlite3_open").value
    sqlite3_open_fp = CFUNCTYPE(ctypes.c_int,
        ctypes.c_char_p, ctypes.c_void_p)(sqlite3_open_ptr)
    return sqlite3_open_fp(uri, None)

def sqlite3_open_uri_ptr(uri):
    sqlite3_open_ptr = ctypes.c_void_p.in_dll(
        sqlite3, "sqlite3_open_v2").value
    sqlite3_open_fp = CFUNCTYPE(
        ctypes.c_int, ctypes
