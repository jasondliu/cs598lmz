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

sqlite3.sqlite3_enable_shared_cache(1)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))
lib.sqlite3_shutdown()

lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))
lib.sqlite3_initialize()
lib.sqlite3_enable_shared_cache(1)

lib.sqlite3_open_v2(b"test", ctypes.byref(my_threading_local.conn), ctypes.c_int(2), None)
lib.sqlite3_create_function_v2(my_threading_local.conn, b"test", 2, ctypes.c_int(0), None, test_fn, None, None, None)
lib.sqlite3_close(my_threading_local.conn)

lib.sqlite3_open_v2(
