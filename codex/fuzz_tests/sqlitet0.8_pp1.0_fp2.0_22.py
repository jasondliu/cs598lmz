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

libt = ctypes.CDLL(ctypes.util.find_library("thread"))
if libt:
    libt.pthread_create.restype = ctypes.c_int

efn = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
if efn:
    efn.sqlite3_exec.argtypes = [ ctypes.c_void_p,
                                  ctypes.c_char_p,
                                  ctypes.c_void_p,
                                  ctypes.c_void_p,
                                  ctypes.POINTER(ctypes.c_char_p) ]

def test_execcallback_threads():
    if not libt:
        return
    if not efn:
        return

    global my_threading_local
    a = sqlite3.connect(DB_URI, uri=True)
    a.creat
