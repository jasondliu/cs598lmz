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

# create the callback function
cb_functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cb_func = cb_functype(my_cb)

# store in our thread local data
my_threading_local.cb_func = cb_func

def my_callback_fnp(p):
    cb_func = my_threading_local.cb_func
    return cb_func(p)


# create a callback function pointer
cb_fnptype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cb_fnp = cb_fnptype(my_callback_fnp)

# load the library via ctypes.util.find_library
lib_path = ctypes.util.find_library('sqlite3') or 'sqlite3'
lib_sqlite = ctypes.CDLL(lib_path)

# get the sqlite3 functions we will use
sqlite3_open_v2 = lib_sql
