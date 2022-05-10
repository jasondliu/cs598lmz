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

if __name__ == '__main__':
    ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_config(4, my_cb, 0)

    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.b = b

    b.execute("select test(1, 2)")
    print(my_threading_local.b)

    b.close()
    print(my_threading_local.a)
