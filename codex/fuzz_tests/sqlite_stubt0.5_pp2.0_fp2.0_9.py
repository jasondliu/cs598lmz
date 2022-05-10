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

ctypes.pythonapi.PyEval_InitThreads()

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.pthread_create.argtypes = [
    ctypes.POINTER(ctypes.c_void_p),
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p
]

def thread_fn(p):
    my_threading_local.a.execute("select test(1, 2)")

tid = ctypes.c_void_p()
libc.pthread_create(ctypes.byref(tid), None, thread_fn, None)

sqlite3.enable_callback_tracebacks(True)
sqlite3.enable_shared_cache(True)
sqlite3.threadsafety = 2

conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
conn.create_function("my_cb", 0, my_cb)
conn
