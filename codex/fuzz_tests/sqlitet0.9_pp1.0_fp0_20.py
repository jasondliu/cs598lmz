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

def my_cb2(a, b):
    return a

SQLITE_CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

# Load the SQLite library
sqlite_lib = ctypes.util.find_library("libsqlite3.dylib")
_sqlite = ctypes.cdll.LoadLibrary(sqlite_lib)
byref = ctypes.byref
byval = ctypes.c_void_p

_handle = _sqlite.sqlite3_open(b":memory:", byref(ctypes.c_void_p()))
_sqlite.sqlite3_create_function(
    _handle,
    b"test",
    2,
    ctypes.c_int(sqlite3.SQLITE_UTF16),
    None,
    my_cb2,
    None,
    None)
_sqlite.sqlite3_create_function(
    _handle,
    b"cb",
    0,
    ctypes.c_int
