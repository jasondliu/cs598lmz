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
    for i in range(2000):
        my_threading_local.a.execute("SELECT test(1, 1)").fetchone()

    return 1

if __name__ == "__main__":
    sqlite3.enable_callback_tracebacks(True)

    lib = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
    pthread_create = lib.pthread_create
    pthread_create.argtypes = [ctypes.POINTER(ctypes.c_void_p),
                               ctypes.c_void_p,
                               ctypes.c_void_p,
                               ctypes.c_void_p]
    pthread_create.restype = ctypes.c_int

    pthread_exit = lib.pthread_exit
    pthread_exit.argtypes = [ctypes.c_void_p]
    pthread_exit.restype = None

    class stack_t(ctypes.Structure):
        _fields
