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

sqlite3.sqlite3_set_autocommit(ctypes.c_int(0))

myTest = ctypes.CDLL(ctypes.util.find_library("test_threading"))
assert myTest.Test(ctypes.c_int(1)) == 17
print("test finished")
</code>
output:
<code>test finished
Exception ignored in: &lt;function Connection.__del__ at 0x109e071e0&gt;
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/sqlite3/__init__.py", line 501, in __del__
    dbapi2.Connection.close(self)
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread.The object was created in thread id 140596093438848 and this is thread id 140596093438848.

Process finished with exit code 0
</code>

