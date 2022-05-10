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

def test_fn(a, b):
    return a

def main():
    # Load the sqlite3 module
    sqlite3.sqlite_version_info

    # Register the callback
    sqlite3.sqlite3_set_authorizer(my_cb, None)

    # Create a connection
    conn = sqlite3.connect(DB_URI, uri=True)

    # Create a function
    conn.create_function("test", 2, test_fn)

    # Run a query
    conn.execute("SELECT test(1, 2)").fetchall()

    # Close the connection
    conn.close()

    # Check that the connection is closed
    assert my_threading_local.a.closed

    # Check that the authorizer callback is still registered
    assert sqlite3.sqlite3_set_authorizer(None, None) == my_cb

if __name__ == "__main__":
    main()
