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
    import sqlite3ct as sqlite3ct
    sqlite3ct.register_dynamic_extension(ctypes.CDLL(ctypes.util.find_library("test")), "test", my_cb, None)

    con = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    cur = con.cursor()
    cur.execute("SELECT test(3, 4)")
    assert cur.fetchone() == (3,)
