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
    clib = ctypes.CDLL(ctypes.util.find_library("c"))
    p = ctypes.c_void_p(0)
    clib.malloc.restype = ctypes.c_void_p
    p = clib.malloc(10)

    cb_fn = sqlite3.SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION
    sqlite3.sqlite3_db_config(p, cb_fn, 1)
    sqlite3.sqlite3_enable_load_extension(p, 1)

    #sqlite3.sqlite3_set_authorizer(p, my_cb)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    a.enable_load_extension(True)

    a.load_extension("test", "test_fn")
    a.load_extension("test")
    a.create_function("test", 2, my_cb)
    a.close()
