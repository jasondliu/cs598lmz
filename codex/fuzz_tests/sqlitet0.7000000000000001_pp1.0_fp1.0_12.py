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

def my_cb2(a, b, c, d):
    my_threading_local.a.close()

my_cb_p = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
my_cb_p2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(my_cb2)

sqlite3.sqlite3_shutdown()
sqlite3.sqlite3_config(ctypes.c_int(sqlite3.SQLITE_CONFIG_SINGLETHREAD), None)
sqlite3.sqlite3_initialize()
sqlite3.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.pointer(sqlite3.sqlite3_vfs_find("unix").contents.xOpen(None, DB_URI.encode("utf-
