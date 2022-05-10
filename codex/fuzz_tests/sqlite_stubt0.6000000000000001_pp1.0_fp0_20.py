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

sqlite3.sqlite3_open_v2(DB_URI, ctypes.pointer(my_threading_local.a), 0x0003, None)
sqlite3.sqlite3_progress_handler(my_threading_local.a, 10000, my_cb, None)
my_threading_local.a.execute("create table test(a)")

del my_threading_local.a

import gc
gc.collect()
</code>
What I have tried:

Setting a global variable to the connection object, but it gets garbage collected anyway
Setting the connection object as a property on the callback object
Setting the connection object as a global variable on the callback function

I have tried many more things too, but can't remember them all.
The only thing that works is setting the connection object as a global variable in the callback function, however this is not practical in my use case as there are many different callbacks that need to share the connection object.
So, is there any way to do this?
Edit:
I have discovered that this problem only occurs in Python2.7.10. It
