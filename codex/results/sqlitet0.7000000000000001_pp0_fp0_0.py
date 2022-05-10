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
    my_threading_local.a.execute("select test(1, 2)").fetchall()
    return 1

def my_cb3(p):
    my_threading_local.a.close()
    return 1

def main():
    pthread = ctypes.CDLL(ctypes.util.find_library("pthread"))

    pthread.pthread_create.argtypes = [
        ctypes.POINTER(ctypes.c_void_p),
        ctypes.c_void_p,
        ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p),
        ctypes.c_void_p
    ]

    pthread.pthread_create.restype = ctypes.c_int

    pthread.pthread_join.argtypes = [
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_void_p)
    ]

    pthread.pthread_join.restype =
