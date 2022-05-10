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
    dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    dll.sqlite3_config(5, my_cb, None)
    dll.sqlite3_initialize()

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    cur = conn.cursor()

    cur.execute("select test(123, 456)")
    assert cur.fetchone()[0] == 123

    cur.close()

if __name__ == "__main__":
    main()
