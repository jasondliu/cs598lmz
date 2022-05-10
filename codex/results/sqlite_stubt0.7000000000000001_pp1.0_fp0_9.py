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

sqlite3.sqlite3_auto_extension(my_cb)

def test_init():
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    assert a == my_threading_local.a

    c = a.cursor()

    c.execute("select test('a', 'b')")

    assert c.fetchone() == ('a',)

if __name__ == "__main__":
    test_init()
</code>
I can't seem to find the equivalent in pyodbc.
I've tried using the <code>connect</code> option in the connection string and setting <code>pyodbc.pooling = False</code>, but that doesn't work.
Any help would be appreciated.

