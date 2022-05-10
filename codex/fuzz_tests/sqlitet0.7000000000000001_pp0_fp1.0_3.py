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

def get_mem_addr(ctypes_obj):
    return int(hex(id(ctypes_obj)), 16)


def main():
    p = ctypes.c_void_p()

    sqlite = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    sqlite.sqlite3_open(DB_URI.encode("utf-8"), ctypes.byref(p))
    sqlite.sqlite3_prepare_v2(p, b"SELECT 1", -1, ctypes.byref(p), b"")
    sqlite.sqlite3_step(p)

    sqlite.sqlite3_create_function(p, b"test", 2, 1, ctypes.py_object(my_cb), None, None, None)
    sqlite.sqlite3_prepare_v2(p, b"SELECT test(1, 2)", -1, ctypes.byref(p), b"")
    sqlite.sqlite3_step(p)

    sqlite.sqlite3_finalize
