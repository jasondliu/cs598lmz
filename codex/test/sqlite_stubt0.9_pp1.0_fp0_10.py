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

def get_a():
    if not hasattr(my_threading_local, "a"):
        my_cb(None)
    return my_threading_local.a

def my_collation(a, b):
    if a == b:
        return 0
    else:
        return 1

__thread_handler = ctypes.CDLL(None)
__thread_handler.pthread_key_create.argtypes = (ctypes.POINTER(ctypes.c_void_p),
                                                ctypes.c_void_p)
__thread_key = (ctypes.c_void_p * 1)()
__thread_handler.pthread_key_create(__thread_key, ctypes.py_object(my_cb))
__thread_handler.pthread_setspecific.argtypes = (
    ctypes.c_void_p, ctypes.c_void_p)
__thread_handler.pthread_getspecific.restype = ctypes.c_void_p

