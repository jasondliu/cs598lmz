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
    dll_name = ctypes.util.find_library("sqlite3")
    sqlite3_dll = ctypes.CDLL(dll_name)

    sqlite3_dll.sqlite3_config(7, my_cb, None)

    a = sqlite3.connect(DB_URI, uri=True)
    my_threading_local.a = a

    del sqlite3_dll
    del a
    del my_threading_local
    # at this point the ctypes callback should have triggered
    # and the connection should be closed
</code>

