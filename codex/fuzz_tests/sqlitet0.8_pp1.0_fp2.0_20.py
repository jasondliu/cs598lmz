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

ctypes.CDLL(ctypes.util.find_library("c")).pthread_setspecific(
    ctypes.POINTER(ctypes.c_int)(),
    ctypes.c_void_p(0),
)

threading.Thread(target=my_cb, args=(1,)).start()

while not hasattr(my_threading_local, "a"):
    pass

print(my_threading_local.a)

print(my_threading_local.a.execute("select test(?, ?)", (1, 2)).fetchall())
</code>
I'm running this in python 3.6.8. The log of output is as follows:
<code>&lt;sqlite3.Connection object at 0x7f4d75dd9038&gt;
[(1,)]
</code>
This is followed by a segfault:
<code>Program received signal SIGSEGV, Segmentation fault.

#0  0x0000557c1d1eecfa in ?? () from /usr/lib
