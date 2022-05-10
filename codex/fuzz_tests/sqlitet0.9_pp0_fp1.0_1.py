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

def my_init():
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_auto_extension(my_cb)

my_init()
</code>
This fails with the following output:
<code>Traceback (most recent call last):
  File "./test.py", line 25, in &lt;module&gt;
    my_init()
  File "./test.py", line 19, in my_init
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_auto_extension(my_cb)
  File "/home/gv/Workspaces/python/sqlite3_extension/venv/lib/python2.7/site-packages/ctypes/__init__.py", line 378, in __getattr__
    func = self.__getitem__(name)
  File "/home/gv/Workspaces/python/sqlite3_extension/venv/lib/python2.7/site-packages/ctypes/__init
