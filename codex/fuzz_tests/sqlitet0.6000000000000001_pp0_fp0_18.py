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

sqlite3.sqlite3_open(":memory:", ctypes.byref(my_threading_local.db_ptr))
sqlite3.sqlite3_create_function(
    my_threading_local.db_ptr.value, b"test_cb", 0, None, my_cb
)

sqlite3.sqlite3_exec(my_threading_local.db_ptr.value, b"SELECT test_cb()", None, None)
</code>
This works fine in Python 3.9.0, but fails in 3.8.6, with the following error:
<code>Exception ignored in: &lt;built-in function sqlite3_close&gt;
Traceback (most recent call last):
  File "/usr/local/Cellar/python@3.8/3.8.6/Frameworks/Python.framework/Versions/3.8/lib/python3.8/sqlite3/dbapi2.py", line 468, in close
  File "/usr/local/Cellar/python@3.8/3.8.
