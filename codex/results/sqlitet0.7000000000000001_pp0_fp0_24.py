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

def my_cb2(p):
    my_threading_local.a.close()

    return 1

def main():
    libc = ctypes.CDLL(ctypes.util.find_library("c"))

    libc.pthread_atfork(my_cb, my_cb2, my_cb2)

    pid = os.fork()

    if pid == 0:
        a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        assert a.execute("select test(1);").fetchone()[0] == 1

    else:
        _, status = os.waitpid(pid, 0)
        assert status == 0

main()
