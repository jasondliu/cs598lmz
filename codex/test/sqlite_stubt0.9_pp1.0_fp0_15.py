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

def my_cb2():
    my_threading_local.a.test(1)

    return 1

class InternalError(sqlite3.Error):
    pass

_lib = None

def Setup():
    global _lib
    libname = ctypes.util.find_library("pysqlite3")
    if libname == None:
        raise RuntimeError("Can't find pysqlite3 c library")
    _lib = ctypes.CDLL(libname)

def Test(conn):
    _lib.pysqlite_init.restype = ctypes.c_int
    _lib.pysqlite_init.argtypes = [ctypes.c_int, ctypes.c_void_p,
                                   ctypes.c_void_p, ctypes.c_void_p]
    _lib.pysqlite_init_v2(0, None, None, None)

    conn.create_collati
