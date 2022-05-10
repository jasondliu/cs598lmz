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

sqlite3.enable_shared_cache(True)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

def test_fn(a, b):
    return a

a.create_function("test", 2, test_fn)

my_threading_local.a = a

d = ctypes.CDLL(ctypes.util.find_library("c"))
d.pthread_create.argtypes = [ctypes.POINTER(ctypes.c_long),
                             ctypes.c_void_p,
                             ctypes.c_void_p,
                             ctypes.c_void_p]
d.pthread_create.restype = ctypes.c_int

p = ctypes.pointer(ctypes.c_long())

d.pthread_create(p, None, my_cb, None)

d.pthread_join(p.contents, None)

my_threading_local.a.cursor().execute("select test(1,
