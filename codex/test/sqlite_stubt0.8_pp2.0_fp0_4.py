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
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))

    lib.sqlite3_enable_shared_cache(1)

    p = ctypes.POINTER(ctypes.c_void_p)()

    if lib.sqlite3_open_v2(DB_URI, ctypes.byref(p), 3 | 0x00000200, None) != 0:
        print("Can't open db")
    else:
        conn = ctypes.cast(p, ctypes.POINTER(ctypes.py_object)).contents.value

        lib.sqlite3_db_config(conn, 100, 1, None)

        lib.sqlite3_busy_timeout(conn, 500)

        lib.sqlite3_create_function(conn, "my_cb", 1, 1, ctypes.py_object(my_cb), None, None, None)

        lib.sqlite3_close(conn)

