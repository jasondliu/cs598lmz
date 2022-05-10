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

    return 123


def my_threading_cb(p):
    my_threading_local.a = sqlite3.connect(DB_URI, uri=True)

    def test_fn(a, b):
        return a

    my_threading_local.a.create_function("test", 2, test_fn)

    my_threading_local.a.execute("INSERT INTO test (name) VALUES (test(1,2))")

    return "my_threading_cb"


def my_rc():
    assert(hasattr(my_threading_local, "a"))

    try:
        my_threading_local.a.execute("INSERT INTO test (name) VALUES (test(1,2))")
    except sqlite3.InterfaceError:
        print("DOES NOT WORK")
        return
    print("WORKS")
    return


def thread_cb(p):
    print("cb")

def _thread(cb):
    print("thread_started")
    cb(123)
    print("thread_ended")


