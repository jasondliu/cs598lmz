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

sqlite3.sqlite3_open_v2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p,
                                           ctypes.POINTER(ctypes.c_void_p),
                                           ctypes.c_int, ctypes.c_char_p)(
                                           lambda x, p: 1)
sqlite3.sqlite3_db_config = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p,
                                             ctypes.c_int, ctypes.c_int)(
                                             lambda x, y, z: 1)
sqlite3.sqlite3_close = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(
                        lambda x: 1)
sqlite3.sqlite3_create_function = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p,
                                                  ctypes.c_char_p, ctypes
