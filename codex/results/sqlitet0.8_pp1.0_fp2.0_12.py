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


def test_sqlite_thread_cleanup():
    libc = ctypes.CDLL(ctypes.util.find_library('c'))

    with sqlite3.connect(DB_URI, uri=True, factory=deleting_conn) as conn:
        conn.create_function("test", 1, my_cb)
        conn.execute("SELECT test(1)")

        # Wait for the thread to be joined
        while my_threading_local.a.thread_id not in conn.execute("PRAGMA database_list").fetchall():
            libc.pthread_yield()

        del my_threading_local.a
        gc.collect()
        libc.pthread_yield()

    assert not conn.thread_id in conn.execute("PRAGMA database_list").fetchall()
