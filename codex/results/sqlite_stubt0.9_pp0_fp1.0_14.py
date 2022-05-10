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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"), ctypes.CDLL.RTLD_GLOBAL)
lib.sqlite3_vfs_register(None, 0)
lib.sqlite3_vfs_find("main").contents.xOpen = my_cb
con = sqlite3.connect(DB_URI + "INVALID", uri=True)
cur = my_threading_local.a.cursor()
cur.execute("SELECT test(1, 2)")
</code>
I've created a class which inherits from <code>sqlite3.Connection</code>, and I inherit from that for a reason, I can't create the connection without it, but I also can't override <code>__del__</code> on the base class. But somehow this doesn't work, when running my code, I get the following output:
<code>Unhandled exception in thread started by &lt;function test_function at 0x7ffe6e801b90&gt;
Traceback (most recent call last):
  File "/usr/lib
