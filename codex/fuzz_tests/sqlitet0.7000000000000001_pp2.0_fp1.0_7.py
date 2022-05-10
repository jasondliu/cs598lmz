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

sqlite3.sqlite3_initialize()

sqlite3.sqlite3_shutdown()

libc = ctypes.CDLL(ctypes.util.find_library("c"))

tid = libc.fork()
if tid == 0:
    # we're the child

    sqlite3.sqlite3_shutdown()

    # This causes sqlite3_shutdown to get called again on exit
    libc._exit(0)
else:
    # we're the parent

    _, status = os.waitpid(tid, 0)
    if os.WIFEXITED(status):
        exit_status = os.WEXITSTATUS(status)
        if exit_status != 0:
            raise SystemExit("Child failed with exit status %d" % (exit_status,))

    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_URI, 1)
    sqlite3.sqlite3_config(sqlite3.SQLITE_CONFIG_LOG, my_cb)
    sqlite3.sql
