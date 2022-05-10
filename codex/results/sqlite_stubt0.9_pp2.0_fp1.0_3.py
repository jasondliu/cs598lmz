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

p = ctypes.util.find_library("sqlite3")
assert p, "Cannot find sqlite3 library."

libsqlite3 = ctypes.cdll.LoadLibrary(p)

encoded_uri = '\x01'.join(DB_URI.split("?"))
encoded_uri += "\x00"

libsqlite3.sqlite3_open_v2.argtypes = [
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_void_p),
    ctypes.c_int,
    ctypes.c_char_p]
db = ctypes.c_void_p(0)
r = libsqlite3.sqlite3_open_v2(encoded_uri, ctypes.byref(db), 6, None)

my_threading_local.db = db
libsqlite3.sqlite3_key.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_int]
