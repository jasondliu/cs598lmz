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

my_cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)

if __name__ == "__main__":
    asdf = my_cb_type(my_cb)
    asdf.ctypes
    print(asdf(None))
    if hasattr(my_threading_local, "a"):
        del my_threading_local.a


print("Your program has crashed!")
</code>
What on earth is going on? Why is it not erroring but crashing? EDIT: I noticed it prints out "Your program has crashed!" but if I try to catch the error, it successfully catches the error:
<code>try:
    asdf = my_cb_type(my_cb)
    asdf.ctypes
    print(asdf(None))
    if hasattr(my_threading_local, "a"):
        del my_threading_local.a
except TypeError:
    print("TypeError caught!")
</code>
Which prints out "TypeError caught! Your program
