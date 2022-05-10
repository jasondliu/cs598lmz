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
    conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
    lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library("python3"))
    lib.PyEval_InitThreads()
    lib.PyEval_SaveThread()
    lib.PyEval_ReleaseLock()
    conn.create_function("my_cb", 0, my_cb)
    conn.execute("select my_cb()")
    conn.commit()
    # this line causes a segfault:
    conn.close()

main()
</code>
It will segfault when <code>conn.close()</code> is called, with the following backtrace:
<code>#0  0x00007ffff7bcc5e5 in raise () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x00007ffff7bcfb7b in abort () from /lib/
