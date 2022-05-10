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

def test_callback():
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.set_authorizer(my_cb, my_cb_final)
    conn = sqlite3.connect(DB_URI, uri=True)
    cur = conn.cursor()
    cur.execute("select test(1, 2)")
    conn.close()

class TestCallbacks(unittest.TestCase):
    def test_callback(self):
        test_callback()

if __name__ == '__main__':
    unittest.main()
