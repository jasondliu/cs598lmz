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

def my_cb2(p):
    my_threading_local.a.close()

    return 1

def my_cb3(p):
    return 1

# Assumes that python was compiled with --with-system-expat or
# --with-system-ffi, and thus ctypes.CDLL(None) points to a system ctypes
# implementation.
libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
pthread_create = libc.pthread_create
pthread_create.argtypes = (ctypes.POINTER(ctypes.c_void_p),
                           ctypes.c_void_p,
                           ctypes.c_void_p,
                           ctypes.c_void_p)
pthread_create.restype = ctypes.c_int
pthread_join = libc.pthread_join
pthread_join.argtypes = (ctypes.c_void_p, ctypes.c_void_p)
pthread_join.restype
