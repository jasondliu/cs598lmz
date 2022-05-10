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


def do_something():
    p = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    p.create_function("test_callback", 1, my_cb)

    p.execute("select test_callback(1) from dual")

do_something()
print("after")
</code>
And here's the C backtrace:
<code>(gdb) bt
#0  0x00007ffff689ef0f in raise () at /usr/lib/libc.so.6
#1  0x00007ffff68a0e7e in abort () at /usr/lib/libc.so.6
#2  0x00007ffff797d0b9 in __gnu_cxx::__verbose_terminate_handler() () at /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#3  0x00007ffff7976e54 in ?? () at /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#4  0x00007
