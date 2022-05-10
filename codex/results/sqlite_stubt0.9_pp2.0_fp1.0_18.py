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

def test_call():
    my_threading_local.a.cursor().execute("select test(9, 5)")

wrap_lib = ctypes.util.find_library("unistd_wrap")
lib = ctypes.CDLL(wrap_lib) or ctypes.CDLL("libunistd_wrap.so")
cb_fn = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_void_p))(my_cb)
lib.wrap_main.argtypes = (cb_fn, ctypes.c_void_p)
lib.wrap_main(cb_fn, None)

test_call()

sqlite3.connect(DB_URI, uri=True)
