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

def my_cb_quota(p):
    a = my_threading_local.a
    del my_threading_local.a

    return 1

dll_name = ctypes.util.find_library('libsqlite3')
if dll_name is None:
    print "Couldn't find sqlite3 library"
    sys.exit(1)

lib_sqlite3 = ctypes.CDLL(dll_name)

lib_sqlite3.sqlite3_create_function_v2.argtypes = [ctypes.c_void_p, ctypes.c_char_p, \
                                                   ctypes.c_int, ctypes.c_int, \
                                                   ctypes.c_void_p, ctypes.c_void_p, \
                                                   ctypes.c_void_p, ctypes.c_void_p]

lib_sqlite3.sqlite3_create_function_v2.restype = ctypes.c_int

lib_sqlite3.sqlite3_prepare
