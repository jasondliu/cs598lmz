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

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

a.create_function("my_cb", 1, my_cb)

my_threading_local.a = a
</code>
This program works fine under python 3.1
But on python 2.7, the python interpreter crashes.
Any clue ?


A:

After some more tests with python, I've discovered that this issue seem related to the python garbage collector.
I had to add the following calls
<code>a.enable_shared_cache(True)
</code>
and
<code>sqlite3.sqlite3_enable_shared_cache(True)
</code>
in order for the interpreter not to crash.
I will still try to understand why.

