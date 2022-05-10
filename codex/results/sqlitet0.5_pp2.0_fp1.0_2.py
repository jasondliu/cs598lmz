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
    ctypes.CDLL(ctypes.util.find_library("sqlite3"), use_errno=True).sqlite3_open(DB_URI, ctypes.byref(my_threading_local.db_ptr))
    my_threading_local.db_ptr.contents.pVfs.contents.xSetSystemCall.value(my_cb)

    my_threading_local.a.execute("SELECT test(1,2)")

if __name__ == '__main__':
    main()
</code>
Here is a backtrace:
<code>(gdb) bt
#0  0x00007ffff7b6e425 in raise () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x00007ffff7b70b8b in abort () from /lib/x86_64-linux-gnu/libc.so.6
#2  0x00007ffff7b4f4ee in __libc_message () from /lib/x86_64-linux-gnu
