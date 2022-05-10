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

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.atexit(my_cb)

# This is the line that triggers the issue.
# If it is commented out, the issue does not occur.
libc.atexit(my_cb)

# This is the line that triggers the crash.
# If it is commented out, the issue does not occur.
libc.exit(0)
</code>
The problem seems to be that the <code>sqlite3.Connection</code> object is not being garbage collected.
I have tried to force garbage collection with the following code, but it does not seem to work:
<code># Force garbage collection
import gc
gc.collect()
</code>
I have also tried to call <code>libc.exit()</code> from a different thread, but it does not seem to make a difference.
I have tried to reproduce the issue with the Python 3.7.0 interpreter and the Python 3.7.0 interpreter built with debug symbols, but I was not able to reproduce the issue.
I have also tried
