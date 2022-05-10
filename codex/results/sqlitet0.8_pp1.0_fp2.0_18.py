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

def test_func():
    c = sqlite3.connect(":memory:", uri=True, factory=deleting_conn)
    c.create_function("my_cb", 1, my_cb)
    c.execute("SELECT my_cb(?);", (-1,))

    c.close()

    return 1

ll = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c"))

ll.mmap(None, 4096, ll.PROT_READ | ll.PROT_WRITE, ll.MAP_PRIVATE | ll.MAP_ANONYMOUS, -1, 0)

ctypes.CDLL("libpthread.so.0").pthread_key_create(ctypes.byref(ctypes.c_long()))

t = threading.Thread(target=test_func)
t.start()
t.join()

del t
del my_threading_local.a
</code>
I get this error:
<code>python3 test.py
[8]: *** Error in `
