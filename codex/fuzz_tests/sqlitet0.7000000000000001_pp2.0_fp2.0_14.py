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

a = sqlite3.connect(DB_URI, uri=True)
a.create_function("my_cb", 1, my_cb)
a.execute("select my_cb(1)")

# this is the line that will crash
my_threading_local.a.execute("select test(1,2)")
</code>
If I remove the line this is the line that will crash, then everything works fine. On the other hand, if I replace a.execute("select my_cb(1)") with a.execute("select my_cb(1)")*10 + 1, everything still works fine.
I've run this code on Mac OS X and Windows with both the pysqlite and the sqlite3 module. I have the same problem with both the official python distribution and with Anaconda (although I have a slightly different error message when running the code from Anaconda).
Here's the error message I'm getting on Mac OS X (with the official python distribution and the pysqlite module):
<code>$ python sqlite_test.py 
/Library/Frameworks/Python.framework/
