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

def additional_test(test, travis):
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_enable_shared_cache(0)

    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.execute("create table test(id int)")
    cursor = conn.execute("select * from test")
    conn.set_progress_handler(my_cb, 100)
    cursor.fetchall()

    a = my_threading_local.a
    test.assertEqual(a.total_changes, 0)
    test.assertEqual(a.in_transaction, False)

class ProgressHandlerThreadingTests(unittest.TestCase):
    def test_progress_handler_threading(self):
        lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
        lib.sqlite3_enable_shared_cache(0)

        with sqlite3.connect(DB_
