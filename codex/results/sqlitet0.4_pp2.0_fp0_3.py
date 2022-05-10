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
lib.sqlite3_config(ctypes.c_int(1), ctypes.c_int(1))
lib.sqlite3_initialize()
lib.sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(my_threading_local.db), ctypes.c_int(1), ctypes.c_char_p(None))

lib.sqlite3_set_authorizer(my_threading_local.db, my_cb, ctypes.c_void_p(0))

lib.sqlite3_prepare_v2(my_threading_local.db, "select test(1, 2)".encode("utf-8"), -1, ctypes.byref(my_threading_local.stmt), ctypes.c_char_p(None))
lib.sqlite3_step(my_threading_local.stmt)

lib.sqlite3_finalize(my
