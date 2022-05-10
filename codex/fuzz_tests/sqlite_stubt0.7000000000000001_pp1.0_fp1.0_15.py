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

# get the sqlite3 C library
sqlite3_lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
# make a C callback out of the python function
my_cb_c = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
# register the callback
sqlite3_lib.sqlite3_status(1, my_cb_c, None)

# create a connection and register the function
a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.close()

# make sure user-defined functions are not leaked
assert not hasattr(my_threading_local, 'a')
