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

_libc = ctypes.CDLL(ctypes.util.find_library("c"))

old_thread_start_func = _libc.pthread_create

class my_thread_start_func(_libc.pthread_create):
    def __call__(self, *args):
        thread_start_func = old_thread_start_func.__get__(self)
        return thread_start_func(my_cb, None)

try:
    pthread_create = _libc.pthread_create
    _libc.pthread_create = my_thread_start_func
except (TypeError, AttributeError, KeyError):
    pthread_create = None

print(ctypes.cast(ctypes.pointer(_libc.pthread_create), ctypes.POINTER(ctypes.CFUNCTYPE(None, ctypes.c_void_p)))[0](ctypes.c_void_p()))

