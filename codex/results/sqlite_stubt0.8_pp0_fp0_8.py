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

def my_func():
    b = my_threading_local.a.execute("SELECT test('abc', 'abc')").fetchall()[0][0]
    assert(b == 'abc')

sqlite3.sqlite3_open(DB_URI.encode(), ctypes.byref(my_threading_local.db))
sqlite3.sqlite3_create_function(my_threading_local.db, b"my_cb", -1, 1, ctypes.c_void_p(0), my_cb, None, None)
sqlite3.sqlite3_exec(my_threading_local.db, b"SELECT my_cb()", None, 0)

threading.Thread(target=my_func).start()
</code>
I expect this to execute the function and print <code>abc</code>, but instead I get no results and the following stacktrace:
<code>Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python3.9/threading.py", line
