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

libc_name = ctypes.util.find_library("c")
libc = ctypes.CDLL(libc_name)
libc.atexit(my_cb)

a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.execute("select test(1,2)")

del a
</code>
When I run this, I get this:
<code>Thread 1 "python" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff19b8700 (LWP 61272)]
0x00007ffff7d6bd8e in __GI__IO_file_close_it () from /usr/lib/libpthread.so.0
(gdb) bt
#0  0x00007ffff7d6bd8e in __GI__IO_file_close_it () from /usr/lib/libpthread.so.0
#1  0x00007ffff7b2ba5c in __GI_fflush () from /usr/lib/libc
