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

my_cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
lib.sqlite3_config(ctypes.c_int(2), my_cb_type(my_cb), ctypes.c_void_p())

if __name__ == '__main__':
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.executescript("""
    create table test(id, data);
    insert into test(id, data) values (1, 'test');
    """)

    conn.close()
    conn = None

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    try:
        print(conn.execute("select test(id, data) from test").fetchall())
    finally:
        conn.close()
        conn = None

