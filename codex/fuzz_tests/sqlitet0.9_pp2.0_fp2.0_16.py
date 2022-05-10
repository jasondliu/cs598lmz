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

if __name__ == "__main__":
    rowidfunc = ctypes.pythonapi.sqlite3_last_insert_rowid
    r = ctypes.c_int64(0)
    rowidfunc.argtypes = [ctypes.c_void_p]
    rowidfunc.restype = ctypes.c_int64

#     path = ctypes.util.find_library('sqlite3')
#     lib = ctypes.CDLL(path)

    conn = None
    lib = ctypes.pythonapi.PyCObject_AsVoidPtr(sqlite3._sqlite)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    lib.sqlite3_open(":memory:", ctypes.byref(classify(conn)))
    lib.sqlite3_create_function(conn,
