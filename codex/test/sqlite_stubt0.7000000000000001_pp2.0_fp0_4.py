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
    fn = ctypes.util.find_library("sqlite3")
    if not fn:
        raise Exception("sqlite3 not found")
    sqlite3 = ctypes.CDLL(fn)

    my_cb_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))
    my_cb_c = my_cb_c(my_cb)

    sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.db))
    sqlite3.sqlite3_create_function_v2(my_threading_local.db, "my_cb", -1,
                                       sqlite3.SQLITE_UTF8, None, my_cb_c, None, None, None)
    sqlite3.sqlite3_exec(my_threading_local.db, "SELECT my_cb()", None, None, None)

