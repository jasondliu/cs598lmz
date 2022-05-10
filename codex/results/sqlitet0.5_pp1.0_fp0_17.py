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

sqlite3.sqlite3_initialize()

libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
libpthread = ctypes.CDLL(ctypes.util.find_library("pthread"), use_errno=True)

class c_void(ctypes.Structure):
    pass

class c_int(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int)]

c_int_p = ctypes.POINTER(c_int)

libc.malloc.restype = ctypes.c_void_p
libc.malloc.argtypes = [ctypes.c_size_t]
libc.free.restype = None
libc.free.argtypes = [ctypes.c_void_p]

libpthread.pthread_create.restype = ctypes.c_int
libpthread.pthread_create.argtypes = [
    ctypes.POINTER(ctypes.c_void_p),
