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

if __name__ == "__main__":
    filename = ctypes.util.find_library("sqlite3")
    if not filename:
        raise Exception("sqlite3 library not found")

    sqlite3_dll = ctypes.CDLL(filename)
    sqlite3_dll.sqlite3_set_authorizer.argtypes = [ctypes.c_void_p,
            ctypes.c_void_p, ctypes.c_int]

    result = sqlite3_dll.sqlite3_set_authorizer(None, my_cb, None)
    if result:
        raise Exception("sqlite3_set_authorizer returned %d" % result)

    result = sqlite3_dll.sqlite3_open_v2(DB_URI.encode("utf-8"), None, 0,
            None)
    if result:
        raise Exception("sqlite3_open returned %d" % result)
</code>
Unfortunately, the <code>sqlite3.Connection</code> instance is not getting deleted.
I tried to figure out if
