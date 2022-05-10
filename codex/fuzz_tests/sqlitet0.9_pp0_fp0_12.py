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

if __name__ == '__main__':
    # Make a memory database so we can share it over sqlite3.Connection
    # instances.
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.execute("CREATE TABLE test(a, b)")

    # This is the initial user function.
    conn.create_function("my_cb", 1, my_cb)

    # Test that this works
    conn.execute("INSERT INTO test(a, b) VALUES (1, my_cb(?))", (-999,)).fetchall()

    # This blows up
    # In Python 2.7 we immediately crash. In Python 3 we first get a
    # SystemError before the crash on some platforms.
    # This test checking for both.
    try:
        conn.execute("INSERT INTO test(a, b) VALUES (2, my_cb(?))", (-999,)).fetchall()
    except (sqlite3.OperationalError, SystemError):
        pass
    else:
