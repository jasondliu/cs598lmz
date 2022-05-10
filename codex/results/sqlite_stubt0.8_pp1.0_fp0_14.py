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

    return 100


def my_cb2(a):
    print(a)
    return "hello"

def my_cb3(a):
    print(a)


def my_cb5(a,b,c):
    assert c == 'abc'
    return a

def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

    # the second parameter to sqlite3_create_function_v2 is the name of the
    # module containing the callback.  this is important because when the
    # module is unloaded, python won't call the destructor for the callback
    # class, but the destructor is needed so we can decref the callback
    # function.  so if we use a unique module name each time, the old
    # function object will be gc'ed (but not called) and the new one will be
    # created.  the old module will hang around in memory and a warning will
    # be printed, but that's not worse than the segfault we would get if we
    # didn't do this.
   
