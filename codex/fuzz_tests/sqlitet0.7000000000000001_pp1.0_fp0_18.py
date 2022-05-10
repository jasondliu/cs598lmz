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

class MyThread(threading.Thread):
    def run(self):
        b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        b.set_progress_handler(my_cb, 100)
        b.create_function("test", 2, test_fn)
        b.execute("select test()")
        b.close()

def test_functools_partial():
    lib = ctypes.CDLL(ctypes.util.find_library("c"))

    if hasattr(lib, "malloc"):
        lib.malloc.restype = ctypes.c_void_p
        lib.malloc.argtypes = [ctypes.c_size_t]
        lib.free.argtypes = [ctypes.c_void_p]

    # This should not raise an exception
    lib.malloc(1)

    # This should not raise an exception
    lib.malloc(1)

def test_threads():
    threads = []
    for i in range(10):
       
