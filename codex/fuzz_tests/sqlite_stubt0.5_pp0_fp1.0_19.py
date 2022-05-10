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

def my_cb_2(p):
    my_threading_local.a.close()
    return 1

def my_cb_3(p):
    my_threading_local.a.execute("select test(1, 2)")
    return 1

def test_callback():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_initialize()
    lib.sqlite3_config(ctypes.c_int(3), ctypes.c_int(1))

    lib.sqlite3_create_function_v2(ctypes.c_void_p(), b"test_cb",
            ctypes.c_int(0), ctypes.c_int(1), ctypes.c_void_p(),
            ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb), None, None)

    lib.sqlite3_create_function_v2(ctypes.c_void_p(), b"test_
