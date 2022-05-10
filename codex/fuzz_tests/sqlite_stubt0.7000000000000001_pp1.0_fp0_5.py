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
    ctypes.CDLL(ctypes.util.find_library('Z3Py'))._Z3Py_registerCallback(my_cb)
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    my_threading_local.a = a
    a.close()
    del my_threading_local.a

main()
</code>
Which gives the following error:
<code>$ python test.py
Fatal Python error: PyThreadState_Get: no current thread

Current thread 0x00007f6b4c01d740 (most recent call first):
  File "test.py", line 30 in my_cb
  File "test.py", line 21 in main
  File "test.py", line 23 in &lt;module&gt;
[1]    27757 abort (core dumped)  python test.py
</code>
I would prefer not to use any global variables. I tried using the <code>threading.local</code> object, but I don't understand how to make
