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

sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_MULTITHREAD)

sqlite3.sqlite3_initialize()
sqlite3.enable_shared_cache(True)

conn = sqlite3.connect(DB_URI, uri=True)

libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c"))
libc.malloc.restype = ctypes.c_void_p
p = libc.malloc(20)
libc.malloc.argtypes = [ctypes.c_size_t]

my_cb(p)

def f():
    host = my_threading_local.a
    my_threading_local.a = None
    lock = threading.Lock()
    lock.acquire()
    host.execute("SELECT test(1,2)")
    lock.release()
    try:
        print threading.currentThread(), host
    finally:
        my_threading_local.a = host

for i in range
