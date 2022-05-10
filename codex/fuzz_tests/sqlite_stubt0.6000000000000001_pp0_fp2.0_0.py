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
    ctypes.cdll.LoadLibrary(ctypes.util.find_library("sqlite3")).\
        sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)

    con = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    con.create_function("my_cb", 1, my_cb)

    with con:
        con.executescript("""
        CREATE TABLE t1(a);
        INSERT INTO t1 VALUES(1);
        """)

        con.execute("SELECT my_cb(1)")

        assert con.execute("SELECT test(a, 1) FROM t1").fetchall() == [(1,)]

        con.execute("SELECT my_cb(1)")

        assert con.execute("SELECT test(a, 1) FROM t1").fetchall() == [(1,)]

if __name__ == "__main__":
    main()
