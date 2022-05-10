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

lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))

lib.sqlite3_config(1, my_cb, None)
</code>
And this is the output of <code>valgrind</code>:
<code>==8913== LEAK SUMMARY:
==8913==    definitely lost: 176 bytes in 1 blocks
==8913==    indirectly lost: 0 bytes in 0 blocks
==8913==      possibly lost: 0 bytes in 0 blocks
==8913==    still reachable: 0 bytes in 0 blocks
==8913==         suppressed: 0 bytes in 0 blocks
</code>
Here's the output of <code>gdb python</code>:
<code>(gdb) run
Starting program: /usr/bin/python
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff74d5c5b in pthread_once () from /
