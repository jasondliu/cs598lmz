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

# For some reason test_py_connection_callback_with_create_function_2.py
# needs a database opened before the callback is registered.
#
# This is because the sqlite3 module tries to create a Connection object
# for the database when the callback is registered, and that fails.
#
# The Connection object needs to be created by the library (so it's
# not a python object), and that needs a database to be opened
# beforehand.
a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

sqlite3.sqlite3_open.restype = ctypes.c_int
sqlite3.sqlite3_open.argtypes = (ctypes.c_char_p,)

sqlite3.sqlite3_close.argtypes = (ctypes.c_void_p,)

sqlite3.sqlite3_config.restype = ctypes.c_int
sqlite3.sqlite3_config.argtypes = (ctypes.c_int, ctypes.c_void_p)


