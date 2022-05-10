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

# We must call sqlite3_open_v2 with URI=True, otherwise the test fails.
# We must load the SQLite library explicitly.
sqlite3.load_dll(ctypes.util.find_library("sqlite3"))

# The following statement fails if we use the default sqlite3.Connection
# class in the callback function (see above).
sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(ctypes.c_void_p()), 1, None)
