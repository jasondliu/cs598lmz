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
    ctypes.CDLL(ctypes.util.find_library('c')).srand(0)
    sqlite3.enable_callback_tracebacks(True)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
    sqlite3.sqlite3_collation_needed(None, my_cb)

    c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    c.create_function("rand", 0, lambda: random.randint(0, 255))
    c.execute("select rand()")
</code>
<code>$ python3 test.py
Traceback (most recent call last):
  File "test.py", line 26, in &lt;module&gt;
    c.execute("select rand()")
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 140637192264576 and this is thread
