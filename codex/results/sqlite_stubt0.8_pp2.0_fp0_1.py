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
    cb = sqlite3.sqlite3_progress_handler(my_cb, 10)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.set_progress_handler(cb, 10)

    my_threading_local.conn = conn
    del conn

    fn = ctypes.util.find_library("sqlite3") or "libsqlite3.so.9"
    lib = ctypes.CDLL(fn)

    lib.sqlite3_close(my_threading_local.a._sqlite_conn)


if __name__ == "__main__":
    main()
