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
    ctypes.CDLL(ctypes.util.find_library("c")).free.restype = None

    sqlite3.enable_callback_tracebacks(True)
    sqlite3.sqlite3_profile(my_cb, None)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    for i in range(0, 100):
        conn.execute("select test(?, ?)", (i, i + 1))
        del my_threading_local.a

if __name__ == "__main__":
    main()
