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

def my_cb2(p):
    print(my_threading_local.a.execute("select test(1, 2)"))
    return 1

def my_cb3(p):
    print(my_threading_local.a.execute("select test(1, 2)"))
    return 1

x = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
x.sqlite3_open(DB_URI.encode("ascii"), ctypes.byref(ctypes.c_void_p()))
x.sqlite3_create_function(ctypes.c_void_p(), b"my_cb", None, 0)

threading.Thread(target=my_cb).start()

threading.Thread(target=my_cb2).start()
threading.Thread(target=my_cb3).start()
</code>
In the above example I print from both the second and third thread, though only one prints successfully, the other fails with:
<code>  File "/usr/lib64/python3.7
