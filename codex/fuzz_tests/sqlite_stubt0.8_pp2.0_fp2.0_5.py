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

_lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('sqlite3'))
sqlite3_open_v2 = _lib.sqlite3_open_v2
sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]

def test_thread_sqlite3_multiple_open():
    db = ctypes.c_void_p()
    sqlite3_open_v2(DB_URI.encode(), ctypes.pointer(db), 0x00000004, None)
    _db = sqlite3.Connection._handle_from_c(db)
    _db.set_authorizer(my_cb)

    assert my_threading_local.a

    del my_threading_local.a

    _lib.sqlite3_close(_db)
