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

    return 100
    #return a

def my_cb_for_pthread_key_create(p):
    if not hasattr(my_threading_local, 'a'):
        my_cb(p)

    return 100
    #return my_threading_local.a

def thread_main(p):
    pthread_atfork(my_cb, my_cb_for_pthread_key_create, my_cb)

if True:
    pthread = ctypes.CDLL(ctypes.util.find_library('pthread'))

    pthread_atfork = pthread.pthread_atfork
    pthread_atfork.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
    pthread_atfork.restype = ctypes.c_int

    #my_cb_cb = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)
    #my_cb_cb.restype = ctypes.
