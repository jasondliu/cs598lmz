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

def my_cb2(p):
    a = my_threading_local.a

    # This will crash if the connection is not properly closed
    a.close()

    return 1

def main():
    sqlite3.sqlite3_initialize()

    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb, None)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb2, None)

    a = sqlite3.connect(DB_URI, uri=True)
    a.execute("SELECT test(1, 2)")
    a.close()

    sqlite3.sqlite3_shutdown()

if __name__ == "__main__":
    main()
