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
    sqlite3.enable_callback_tracebacks(True)

    # Without the buffer, the traceback string is empty. There is a
    # buffer of size 256 bytes, but it is not enough.
    #
    # The buffer is located here:
    #
    #  https://github.com/python/cpython/blob/master/Modules/_sqlite/cursor.c#L101
    #
    # We will use ctypes to allocate a larger buffer.
    #
    # For the buffer size, we can use the size of the `_sqlite_api`
    # structure defined in the _sqlite module source code:
    #
    #  https://github.com/python/cpython/blob/master/Modules/_sqlite/module.c#L87
    #
    # Usually, the traceback string is smaller than the size of the
    # `_sqlite_api` structure, so it will fit. In the worst case, it
    # will be truncated.
    #
    # The buffer is used to store the trace
