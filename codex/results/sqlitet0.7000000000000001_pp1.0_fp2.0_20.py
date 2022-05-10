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

p = ctypes.c_void_p()

# libsqlite3 = ctypes.util.find_library("sqlite3")
libsqlite3 = "./libsqlite3.so"
libsqlite3 = ctypes.CDLL(libsqlite3)

libsqlite3.sqlite3_open_v2.restype = ctypes.c_int
libsqlite3.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p]
res = libsqlite3.sqlite3_open_v2(
    DB_URI.encode("utf-8"),
    ctypes.pointer(p),
    1 | 2,
    None,
)
if res != 0:
    raise Exception("sqlite3_open_v2: %s" % res)

sqlite3.sqlite_api = ctypes.cdll.LoadLibrary(libsqlite3._name)
sqlite3.sqlite
