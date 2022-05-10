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

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'), ctypes.RTLD_GLOBAL)

lib.sqlite3_config(ctypes.c_int(5), ffi.NULL)

con = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
conn_ptr = con._conn_ptr
# Acquire a lock, to ensure we keep a reference to our own connection
# so that it isn't closed before sqlite_test_control :)
con.execute("select 1")

lib.sqlite3_test_control(ctypes.c_int(18), ffi.NULL, ffi.NULL, ctypes.c_int(1), ctypes.py_object(lib))

lib.sqlite3_test_control(ctypes.c_int(15), ffi.NULL, ctypes.c_void_p(conn_ptr), ctypes.py_object(my_cb), ffi.NULL)

assert my_threading_local.a is con

print
