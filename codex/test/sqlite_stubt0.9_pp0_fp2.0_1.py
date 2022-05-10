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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
SQLITE_CONSTANT = lib.SQLITE_CONSTANT
lib.sqlite3_initialize()
lib.sqlite3_open(DB_URI, ctypes.byref(ctypes.c_void_p()))
SQLITE_OPEN_DELETEONCLOSE = 0x000010
lib.sqlite3_open_v2(DB_URI, ctypes.byref(ctypes.c_void_p()), SQLITE_OPEN_DELETEONCLOSE, None)
lib.sqlite3_enable_load_extension(ctypes.c_void_p(), 1)
lib.sqlite3_set_authorizer(ctypes.c_void_p(), my_cb(1), None)
lib.sqlite3_exec(ctypes.c_void_p(), "SELECT load_extension('mod_spatialite')", None, None, None)
lib.sqlite3_finalize(ctypes.c_void_p())
