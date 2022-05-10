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
    p = ctypes.c_void_p()
    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c.create_function("test_cb", 1, my_cb)
    print("Calling test_cb")
    c.execute("SELECT test_cb(?)", (p,))
    print("Callback done")
    print("Attempting to access connection from callback...")
    print("Result from test function:", my_threading_local.a.execute("SELECT test(1, 2)").fetchone())
    print("All ok!")

if __name__ == '__main__':
    main()
