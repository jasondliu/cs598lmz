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

def main():
    sqlite3.enable_callback_tracebacks(True)
    cstr = ctypes.create_string_buffer(b"foo")
    f = ctypes.CDLL(ctypes.util.find_library("c"))
    f.cstrtod.argtypes = [ctypes.c_char_p]
    ival = f.cstrtod(cstr)
    print(ival)

main()
</code>
The <code>print(ival)</code> line crashes with a segfault.  I've traced it down to the thread being deleted due to the garbage collection before I've finished with the thread, but I'm not exactly sure how to deal with this.  <code>threading.local</code> returns a threadlocal object, which I've been using in a file context outside of python, but I'm not sure what to do when I create the SQLite connection object in the callbackfn.

