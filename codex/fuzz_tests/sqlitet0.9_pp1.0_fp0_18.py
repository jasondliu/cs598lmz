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

sqlite3.sqlite3_destructor_type

class my_cb_type(ctypes.c_void_p):
    @staticmethod
    def from_param(param):
        if isinstance(param,my_cb_type):
            return param

        # Otherwise, rather than raise an error, just return the NULL pointer
        return None


my_cb_type_pointer = ctypes.POINTER(my_cb_type)

ctl = sqlite3.sqlite3_sqlite3



libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
sqlite = ct.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

print(sqlite.sqlite3_threadsafe())


cb_type = ct.CFUNCTYPE(ctypes.c_int, my_cb_type)
my_cb_func = cb_type(my_cb)

conn_cb_type = ct.CFUNCTYPE(ctypes.c_
