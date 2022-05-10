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

def my_fn(b):
    a = my_threading_local.a.execute("select test(?);", (b,)).fetchone()[0]
    return a

lib = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
lib.my_cb_fn.argtypes = [ctypes.c_void_p]
lib.my_cb_fn.restype = ctypes.c_int
lib.my_cb_fn.errcheck = lib.my_errcheck
lib.my_errcheck.argtypes = [ctypes.c_int]
lib.my_errcheck.restype = None
lib.my_fn.argtypes = [ctypes.c_void_p]
lib.my_fn.restype = ctypes.c_int
lib.my_fn.errcheck = lib.my_errcheck

lib.register_callback(lib.my_cb_fn, my_cb)
assert lib.my_fn(1) == 1
</code>
I'm not sure
