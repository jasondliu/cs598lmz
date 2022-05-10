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


lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))

lib.sqlite3_set_authorizer.restype = ctypes.c_int
lib.sqlite3_set_authorizer.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

my_cb_p = ctypes.CFUNCTYPE(ctypes.c_int)(my_cb)

sqlite3.connect(DB_URI, uri=True).close()

assert lib.sqlite3_set_authorizer(sqlite3.sqlite_api._handle, None, my_cb_p) == 0

try:
    sqlite3.connect(DB_URI, uri=True)
except sqlite3.OperationalError as e:
    assert str(e) == "SQL logic error or missing database"

my_threading_local.a.close()

try:
    sqlite3.connect(DB_URI, uri=
