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

ligsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

#enable shared cache mode
ligsqlite3.sqlite3_enable_shared_cache(1)
ligsqlite3.sqlite3_initialize()

ligsqlite3.sqlite3_open_v2(DB_URI.encode('utf-8'), ctypes.pointer(ctypes.c_void_p()), 0x2, None)

ligsqlite3.sqlite3_api_routines.xbusy_handler.restype = ctypes.c_int

ligsqlite3.sqlite3_api_routines.xbusy_handler.argtypes = [ctypes.c_void_p, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)]

ligsqlite3.sqlite3_busy_handler(ctypes.c_void_p(1), ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_
