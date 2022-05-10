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

if __name__ == '__main__':
    sqlite3.sqlite3_enable_load_extension(True)
    sqlite3.sqlite3_reset_auto_extension()
    lib = ctypes.util.find_library("sqlite3")
    assert lib
    sqlite3.sqlite3_auto_extension(my_cb)

    with sqlite3.connect(DB_URI, uri=True, factory=deleting_conn) as conn:
        cursor = conn.cursor()
        cursor.execute("select test('test', 'test')")
        # If the following line is reached, the bug has healed itself.
        cursor.fetchone()
