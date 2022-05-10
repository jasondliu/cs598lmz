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

def my_cb_final(p):
    my_threading_local.a.close()

    return 1

class SQLiteThreadingTestCase(unittest.TestCase):
    def test_threading(self):
        """See if we can use sqlite in a multi-threaded environment"""
        sqlite3.enable_callback_tracebacks(True)
        sqlite3.set_authorizer(my_cb)
        sqlite3.set_final(my_cb_final)

        def my_thread(n):
            conn = sqlite3.connect(DB_URI, uri=True)
            cur = conn.cursor()
            cur.execute("create table test(a, b)")
            cur.execute("insert into test(a, b) values (?, ?)", (n, n))
            conn.commit()
            cur.execute("select test(a, b) from test")
            self.assertEqual(cur.fetchone()[0], n)
            conn.close()

        threads = [threading.Thread(target=my_
