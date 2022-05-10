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

lib = ctypes.CDLL(ctypes.util.find_library("pthread"))
lib.pthread_create.argtypes = (ctypes.c_void_p,
                               ctypes.c_void_p,
                               ctypes.c_void_p,
                               ctypes.c_void_p)
thread_id = ctypes.c_long(0)
lib.pthread_create(ctypes.byref(thread_id), None, my_cb, None)

while not hasattr(my_threading_local, "a"):
    pass
