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

sqlite3.sqlite3_create_function(my_cb, 1, "test")

if __name__ == "__main__":
    a = sqlite3.connect(DB_URI, uri=True)

    a.execute("select test(1, 2)")

    print a.execute("select test(1, 2)").fetchall()

    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
