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

def my_cb2(p, n):
    a = my_threading_local.a
    r = a.execute("select test(1, 2)").fetchone()
    assert r[0] == 1
    return 1

def my_cb3(p, n):
    a = my_threading_local.a
    r = a.execute("select test(1, 2)").fetchone()
    assert r[0] == 1
    return 1

def main():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.sqlite3_enable_shared_cache(1)
    sqlite3.enable_shared_cache(True)
    sqlite3.threadsafety = 2
    sqlite3.sqlite_version_info = (3, 8, 11)

    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    a.execute("create table test(a, b)")
    a.commit()

    libc = ctypes.CDLL(
