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

def test_1():
    sqlite3.sqlite3_open(":memory:", ctypes.pointer(my_threading_local.a))
    sqlite3.sqlite3_create_module(
        my_threading_local.a, "test", None, my_cb)
    sqlite3.sqlite3_close(my_threading_local.a)

def main():
    print("Probe #1")
    test_1()
    print("Probe #2")

if __name__ == "__main__":
    main()
