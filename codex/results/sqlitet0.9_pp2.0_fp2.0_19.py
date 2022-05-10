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

def main():
    if ctypes.util.find_library("sqlite3"):
        cSQLite = ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3"))
    else:
        cSQLite = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), 'libcSQLite3.dylib'))

    callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)
    cSQLite.sqlite3_open_v2(DB_URI.encode(encoding='ascii', errors='ignore'), ctypes.pointer(ctypes.c_void_p()), 0, None)
    cSQLite.sqlite3_open_v2(DB_URI.encode(encoding='ascii', errors='ignore'), ctypes.pointer(ctypes.c_void_p()), 0, None)
    cSQLite.sqlite3_open_v2(DB_URI.encode(encoding='as
