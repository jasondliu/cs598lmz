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

def my_close_cb(p):
    my_threading_local.a.close()
    return 1

# the actual threading local access:

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_open.argtypes = [ ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p) ]
    lib.sqlite3_open.restype = ctypes.c_int

    v = ctypes.c_void_p()

    if lib.sqlite3_open(DB_URI, ctypes.byref(v)):
        if lib.sqlite3_errcode(v) == 1:
            print "database locked"
            return 1
        print "error", lib.sqlite3_errcode(v)

    lib.sqlite3_set_authorizer(v, my_cb, 0)
    lib.sqlite3_set_close_callback(v, my_close_cb, 0)

   
