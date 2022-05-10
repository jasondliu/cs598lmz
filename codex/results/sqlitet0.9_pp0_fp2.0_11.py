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

    return 123

def create_n_fns(conn, n):
    for i in range(n):
        conn.create_function("fn%d"%i, 1, lambda x: x)

def create_n_aggs(conn, n):
    for i in range(n):
        conn.create_aggregate("agg%d"%i, 1, lambda x: x, lambda x: x)

def create_n_collations(conn, n):
    def collation_fn(x, y):
        return ctypes.pythonapi.PyObject_Compare(x, y)
    collation_fn.restype = ctypes.c_int

    for i in range(n):
        conn.create_collation("collation%d"%i, collation_fn)

if __name__ == "__main__":
    sqlite3.enable_callback_tracebacks(True)
    dll = ctypes.CDLL(ctypes.util.find_library("c"))
    dll.calloc.restype = ctypes.c_void_p
