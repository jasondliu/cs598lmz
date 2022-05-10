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
    cf = ctypes.c_void_p(0)
    if not ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_open_v2(DB_URI.encode("utf-8"), ctypes.byref(cf), 0x0003, None):
        if not ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_create_function_v2(cf, "my_cb", 1, 1, 0, my_cb, 0, 0, 0):
            if not ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_exec(cf, "SELECT my_cb(1);", 0, 0, 0):
                assert my_threading_local.a
                my_threading_local.a.execute("INSERT INTO hello VALUES(?)", (1,))

try:
    main()
except:
    pass


