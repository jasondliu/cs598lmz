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

c = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
c.set_authorizer(my_cb)
c.commit()
c.close()
</code>
This will segfault:
<code>Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff0675700 (LWP 4307)]
0x00007ffff74e0ed5 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
56  ../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  0x00007ffff74e0ed5 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
#1  0x00007ffff74e3b8b in __GI_
