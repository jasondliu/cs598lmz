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


libc = ctypes.CDLL(ctypes.util.find_library("c"))
sqlite_open = libc.sqlite3_open
sqlite_open.restype = int
sqlite_open.argtypes = (ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p))

c = ctypes.c_void_p()
r = sqlite_open(DB_URI.encode("utf-8"), ctypes.byref(c))

lib = ctypes.CDLL("test-ext.so")
lib.my_cb.restype = int
lib.my_cb.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p), ctypes.c_void_p)

test_thread = threading.Thread(target=lib.my_cb, args=(
ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p), c))
test_thread.daemon = True
test_thread.
