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

def test_closed():
    """
    Test that the connection is only closed when the object is destroyed.
    """
    test_lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    test_lib.sqlite3_open(":memory:", ctypes.byref(ctypes.c_void_p()))

    test_lib.sqlite3_create_function(
        my_threading_local.a.connection,
        b"test",
        2,
        1,
        0,
        my_cb,
        0,
        0)

    # The connection should not be closed at this point.
    assert my_threading_local.a.connection._conn.value is not None

    # The connection should be closed when the Connection object leaves scope.

if __name__ == "__main__":
    test_closed()
