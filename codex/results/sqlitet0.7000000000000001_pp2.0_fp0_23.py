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
    # initial test
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    # this should fail because test is not a function
    try:
        a.create_function("test", 2, "test")
    except sqlite3.OperationalError:
        print("first test passed")
    else:
        raise Exception("first test failed")

    # this should fail because test is not a function either
    try:
        a.create_function("test", 2, None)
    except sqlite3.OperationalError:
        print("second test passed")
    else:
        raise Exception("second test failed")

    # this should succeed
    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    # this should fail because test already exists
    try:
        a.create_function("test", 2, test_fn)
    except sqlite3.OperationalError:
        print("third test passed
