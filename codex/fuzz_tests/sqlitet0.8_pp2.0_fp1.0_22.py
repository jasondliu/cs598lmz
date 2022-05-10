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

# The callback itself is written in Python, but the SQLite handler is still
# written in C. This verifies that we do the right thing with the threading
# local in that case too.
c_mod = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
c_mod.sqlite3_thread_cleanup()

(sqlite3
 .connect(DB_URI, uri=True, factory=deleting_conn)
 .enable_load_extension(True)
 .load_extension("./testext/build/lib.macosx-10.14-x86_64-3.7/_test.cpython-37m-darwin.so")
 .enable_callback_tracebacks(True)
 .create_function("test", 3, my_cb))
</code>
Here's the C code for the extension (<code>test.c</code>):
<code>#include &lt;Python.h&gt;
#include &lt;sqlite3ext.h&gt;

static PyObject *cb_p
