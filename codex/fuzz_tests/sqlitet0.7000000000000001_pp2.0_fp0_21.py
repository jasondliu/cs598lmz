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

sqlite3.sqlite3_shutdown()
sqlite3.set_authorizer(my_cb)
sqlite3.sqlite3_initialize()

print my_threading_local.a
</code>
If you run this code, you'll see that <code>my_threading_local.a.close()</code> gets called even though it should be held in the <code>threading.local()</code> object.
Here's the output:
<code>Thread 1: &lt;deleting_conn object at 0x7f821e2c2eb0&gt;
Thread 1: closing
Thread 2: &lt;deleting_conn object at 0x7f821e2c2eb0&gt;
Thread 2: closing
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python2.7/threading.py", line 551, in __bootstrap_inner
    self.run()
  File "test.py", line 33, in run
    print my_threading_
