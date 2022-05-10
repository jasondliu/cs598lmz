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

p = sqlite3.sqlite3_open_v2(DB_URI, ctypes.pointer(ctypes.c_int()),
                            sqlite3.SQLITE_OPEN_READWRITE |
                            sqlite3.SQLITE_OPEN_CREATE |
                            sqlite3.SQLITE_OPEN_URI,
                            ctypes.c_char_p("test"))

sqlite3.sqlite3_progress_handler(p, 1, my_cb, p)

for i in range(10):
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    conn.execute("SELECT test(1, 2)")
    conn.close()
</code>
I get the following error:
<code>python3 test.py
Traceback (most recent call last):
  File "test.py", line 33, in &lt;module&gt;
    conn.execute("SELECT test(1, 2)")
sqlite3.ProgrammingError: Cannot operate on a closed database.
