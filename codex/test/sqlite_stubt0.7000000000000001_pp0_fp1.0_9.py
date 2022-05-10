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
    sqlite3.sqlite3_enable_shared_cache(0)
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.execute("CREATE TABLE test (v INTEGER)")
    conn.execute("INSERT INTO test (v) VALUES (?)", (1,))
    conn.execute("INSERT INTO test (v) VALUES (?)", (2,))
    conn.commit()
    conn.create_function("test", 1, lambda x: x)
    lib.sqlite3_set_authorizer(conn.sqlite_handle, my_cb, None)
    conn.execute("SELECT test(1)")
    conn.execute("SELECT test(1)")
    conn.execute("SELECT test(v) FROM test")
    conn.execute("SELECT test(v) FROM test")

