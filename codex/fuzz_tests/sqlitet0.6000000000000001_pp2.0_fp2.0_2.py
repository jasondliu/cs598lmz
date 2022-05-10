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

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
lib.sqlite3_enable_shared_cache(1)
lib.sqlite3_config(3, my_cb, 0)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.execute("select test(1, 2)")

b = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
b.execute("select test(1, 2)")
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 43, in &lt;module&gt;
    b.execute("select test(1, 2)")
sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 140509518668032 and this is thread id 140509520286720
</code>
Is there any way to pass
