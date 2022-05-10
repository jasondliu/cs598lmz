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
    sqlite3.sqlite3_open_v2(DB_URI, ctypes.byref(my_threading_local.conn),
                            sqlite3.SQLITE_OPEN_READWRITE | sqlite3.SQLITE_OPEN_CREATE |
                            sqlite3.SQLITE_OPEN_URI, None)
    sqlite3.sqlite3_busy_timeout(my_threading_local.conn, 1000)
    my_threading_local.conn.isolation_level = None
    sqlite3.sqlite3_create_function(my_threading_local.conn, b"fn", 1, None, my_cb)
    my_threading_local.conn.close()
    print(my_threading_local.a)

if __name__ == "__main__":
    main()
