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

ctypes.CDLL(ctypes.util.find_library("c")).atexit(my_cb)

def test_fn(b):
    return my_threading_local.a.execute("SELECT test(?, ?)", (1, b))

print(test_fn(2))
print(test_fn(2))
</code>
When I run this code, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 23, in &lt;module&gt;
    print(test_fn(2))
  File "test.py", line 17, in test_fn
    return my_threading_local.a.execute("SELECT test(?, ?)", (1, b))
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread.The object was created in thread id 140242413191168 and this is thread id 140242413191168
</code>
This error is occurring because, according to the source code, sqlite is checking the address of <
