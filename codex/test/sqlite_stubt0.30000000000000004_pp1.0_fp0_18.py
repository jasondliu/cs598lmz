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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.db), sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE | sqlite3.SQLITE_OPEN_URI, None)

my_threading_local.db.contents.pVfs.contents.xOpen.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
my_threading_local.db.contents.pVfs.contents.xOpen.restype = ctypes.c_int
my_threading_local.db.contents.pVfs.contents.xOpen.errcheck = lambda result, func, arguments: result

my_threading_local.db.contents.pVfs.contents.xOpen.errcheck = lambda result, func, arguments: result
my_threading_local.db.contents.pVfs.contents
