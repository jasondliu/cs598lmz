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

def my_thread():
    my_threading_local.a.execute("select test(0, 1.3)").fetchall()

tracer = LoadLibrary("../../build/llvm/lib/libxraytrace")

tracer.test_fn(my_cb)

# this does not raise an exception
a = tracer.test_fn(my_thread)
</code>
Running it looks like this:
<code>$ python llvm_xray_test2.py
^C
Traceback (most recent call last):
  File "llvm_xray_test2.py", line 49, in &lt;module&gt;
    a = tracer.test_fn(my_thread)
KeyboardInterrupt
$
</code>
I did <code>^C</code> to show that this script will run indefinitely.
Any clue as to why this works, but the <code>_ctypes</code> version of it doesn't?

