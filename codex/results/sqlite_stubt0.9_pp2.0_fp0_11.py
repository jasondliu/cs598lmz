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

sqlite3.sqlite3_open(DB_URI, ctypes.byref(my_threading_local.con))
sqlite3.sqlite3_create_function_v2(my_threading_local.con, "test_cb", 1, 1, 0, my_cb, None, None, None, None)

# Check that the created connection has worked.
cur = my_threading_local.a.cursor()
cur.execute("select test(test_cb(0), 1)")
assert cur.fetchone()[0] == 1

# Create a new thread which will use the same connection object.
# Accessing the connection object after the interpreter has shut down
# should not crash.
def one_worker_thread(my_threading_local):
    worker_thread_local = threading.local()
    worker_thread_local.a = my_threading_local.a
    cur = worker_thread_local.a.cursor()
    cur.execute("select test(test_cb(0), 1)")
    assert cur.fetch
