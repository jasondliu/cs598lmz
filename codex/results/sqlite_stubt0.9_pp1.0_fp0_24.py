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

# This tests that when a custom connection factory is used, and a
# callback is registered, the python objects do not leak.
#
# The C++ calls `PyEval_InitThreads()` to initialise threading.

c_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)(my_cb)
libsqlite3 = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
libsqlite3.sqlite3_enable_load_extension(pysqlite_native_connection(), 0)
libsqlite3.sqlite3_load_extension(pysqlite_native_connection(), b"pysqlite_testutils", b"sqlite3_pysqlite_testutils_init", c_cb, None)
libsqlite3.sqlite3_create_function(pysqlite_native_connection(), b"test2", 1, c_cb, None)
cursor = pysqlite_connection().execute("select test(1, 2)")
cursor
