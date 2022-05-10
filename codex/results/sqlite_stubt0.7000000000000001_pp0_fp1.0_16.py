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

    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_load_extension(0, 1)
    lib.sqlite3_create_function_v2(0, "test", 1, 0, 0, ctypes.cast(my_cb, ctypes.c_void_p), 0, 0, 0)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    a.executescript("""
        CREATE TABLE t1 (
            c1 PRIMARY KEY,
            c2
        );

        INSERT INTO t1 VALUES (1, 'one');
        INSERT INTO t1 VALUES (2, 'two');
    """)

    a.execute("SELECT test(c2) FROM t1").fetchall()

    a.close()

if __name__ == '__main__':
    main()
</code>

