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

try:
    libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
except OSError as e:
    pass

try:
    libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True)
except OSError as e:
    pass

my_cb_f = libc.malloc(ctypes.sizeof(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)))
my_cb_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
ctypes.memmove(my_cb_f, ctypes.addressof(my_cb_c), ctypes.sizeof(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)))

