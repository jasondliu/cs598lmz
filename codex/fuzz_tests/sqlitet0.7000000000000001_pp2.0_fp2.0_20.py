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

sqlite3.sqlite3_set_authorizer(my_cb)

# The following statement causes the segfault
sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
</code>
The code above is in the file <code>test.py</code>. When I execute <code>python test.py</code>, I get the following traceback:
<code>Segmentation fault (core dumped)
python test.py
</code>
The output of <code>gdb python test.py</code> is:
<code>Starting program: python test.py
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff4d4c4f4 in _int_free (av=0x7ffff4e71d40 &lt;main_arena&gt;, p=0x7ffff6ff2c50) at malloc.
