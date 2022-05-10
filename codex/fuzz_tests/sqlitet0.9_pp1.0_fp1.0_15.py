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

sqlite_open = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

# this cannot be called more than once in the entire lifetime of a process. it returns an sqlite3* handle, that should *never* get closed
sqlite3_open = sqlite_open.sqlite3_open
sqlite3_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
sqlite3_open.restype = ctypes.c_int

sqlite_handle = ctypes.c_void_p()
sqlite3_open(DB_URI.encode('utf-8'), ctypes.byref(sqlite_handle))


# create a memory database, set the "authorizer" function to my_cb, which is our own python function.
# the threading local data we set in our my_cb function is what's causing a threading lock.
sqlite_create_function = sqlite_open.sqlite3_create_function_v2
sqlite_create_function
