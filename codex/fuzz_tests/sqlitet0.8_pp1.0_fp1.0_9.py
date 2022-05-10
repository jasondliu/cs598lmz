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

sqlite3.sqlite_open_uri(DB_URI, flags=0, vfs=None, uri=False,
    user=None, passwd=None, cb=my_cb, choose_cb=0,
    uri_int64=False, uri_boolean=False,
    uri_decimal=False, uri_double=False,
    uri_none=False)

sqlite3.register_adapter(float, lambda f: sqlite3.Binary(struct.pack(b"!d", f)))
sqlite3.register_converter("float", lambda s: struct.unpack(b"!d", s)[0])

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_open.argtypes = [
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_void_p),
]
lib.sqlite3_open.restype = ctypes.c_int

db = ctypes.c_
