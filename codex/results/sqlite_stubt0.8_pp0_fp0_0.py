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

context = ctypes.CDLL(ctypes.util.find_library("libc"))

p = context.atexit(my_cb)

del p  # create a dangling pointer
del context

print("end")
</code>
This is tested under Python 3.7. Very likely to work on Python 3.6 and possibly Python 2.7 as well, since <code>deleting_conn</code> is a weak reference.
Update:
<code>sqlite3</code> has a default collation function. On Python 3.6, I get the following output, indicating that it doesn't invoke the default collation function, but does invoke the default function for <code>test</code>.
<code>&gt; python3.6 bug.py
default_collate_called 0
test_fn_called 1
&gt;
</code>

