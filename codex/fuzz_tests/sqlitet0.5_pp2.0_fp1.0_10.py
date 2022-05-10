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
    try:
        sqlite3.enable_callback_tracebacks(True)
        sqlite3.set_authorizer(my_cb)
        conn = sqlite3.connect(DB_URI, uri=True)
        conn.cursor().execute("select test(1, 2);")
    finally:
        # The following line is needed to trigger the bug.
        # Without it, the crash does not occur.
        my_threading_local.a.cursor().execute("select 1;")
        # The following line is needed for the crash to occur.
        # Without it, the crash does not occur.
        del my_threading_local.a


if __name__ == "__main__":
    main()
