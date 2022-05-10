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

def main():
    ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_open(DB_URI.encode(), ctypes.byref(my_threading_local.handle))

    if my_threading_local.handle.value:
        ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_close(my_threading_local.handle)
        my_threading_local.handle = None

    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
</code>
The above code works fine with Python 2.7, but using Python 3.6 gives the following error:
<code>Exception ignored in: &lt;bound method deleting_conn.__del__ of &lt;__main__.deleting_conn object at 0x10c8a8b90&gt;&gt;
Traceback (most recent call last):
  File "test.py", line 19, in __del__
  File "test.py", line 27
