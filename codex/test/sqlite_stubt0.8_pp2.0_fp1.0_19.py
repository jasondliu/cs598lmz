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

my_cb_fn = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(my_cb)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.register_extension_functions_for_unittest(my_cb_fn)

def get_cursor():
    return my_threading_local.a.cursor()

def get_connection():
    return my_threading_local.a

lib.run_sql("SELECT 1 + test(2, 3)", get_cursor())
