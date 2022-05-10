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

    return 10


def start_thread():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    """
    After having created a UDF in one connection, we then return from this 
    function to trigger the garbage collector.

    The garbage collector will free the connection that was used to create 
    the UDF.

    The other connection must still be valid.
    """
    b.create_function("test", 2, test_fn)
"""

def main():
    count = 0
    while True:
        if count % 1000 == 0:
            print count

        count += 1

        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

        def test_fn(a, b):
            return a

        a.create_function("test", 2, test_fn)

        a.close()
