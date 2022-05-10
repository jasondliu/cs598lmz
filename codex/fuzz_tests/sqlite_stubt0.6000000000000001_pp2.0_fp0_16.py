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
    libsqlite_path = ctypes.util.find_library("sqlite3")
    libsqlite = ctypes.CDLL(libsqlite_path)
    libsqlite.sqlite3_open_v2.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
    libsqlite.sqlite3_open_v2.restype = ctypes.c_int
    libsqlite.sqlite3_open_v2.errcheck = lambda ret, func, args: SQLITE_OK

    callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    libsqlite.sqlite3_open_v2(":memory:", None, SQLITE_OPEN_READWRITE | SQLITE_OPEN_CREATE | SQLITE_OPEN_URI, callback)

main()
</code>
This is a minimal example of the problem.  I have a
