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

ctypes.CDLL(ctypes.util.find_library("sqlite3")).sqlite3_auto_extension(ctypes.cast(ctypes.CFUNCTYPE(ctypes.c_int)(my_cb), ctypes.c_void_p))

threading.Thread(target=lambda:print("")).start()

print("end")
</code>
This will cause a segfault at the end of the program.


A:

From the SQLite docs on sqlite3_auto_extension:
<blockquote>
<p>SQLite automatically loads extension.</p>
</blockquote>
In this context, "extension" refers to a function initialization function, not to the extension module itself.
The unloaded module can still contain live objects that reference Python objects, which causes the problem you see - so the module needs to stay alive until the thread is done using the module.
As this would leave the module loaded beyond the point that it should be unloaded - so relying on the module being unloaded manually is not an option; you must shut down the thread before unloding the module.

