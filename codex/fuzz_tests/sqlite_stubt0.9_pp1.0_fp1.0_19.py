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

def setup():
    s = sqlite3.connect(":memory:",
                        uri=True,
                        factory=deleting_conn)

    dbapi2.connect = lambda *args, **kwargs: deleting_conn(DB_URI, uri=True)

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    opendb = lib.sqlite3_open_v2
    opendb.argtypes = (ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int,
                       ctypes.c_char_p)

    db = ctypes.c_void_p()
    result = opendb(":memory:", ctypes.byref(db),
                    dbapi2.SQLITE_OPEN_READWRITE | dbapi2.SQLITE_OPEN_CREATE,
                    None)

    if result == dbapi2.SQLITE_ERROR:
        raise sqlite3.Error(ctypes.c_char_p(lib.sqlite3_err
