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

CLibrary = ctypes.CDLL(ctypes.util.find_library("pthread"))
CLibrary.pthread_atfork(None, None, my_cb)

sqlite3.load_extension("./src/libsqlitewrapped.so")

# This is where logging statements seem to output to
sys.stdout.write(str(my_threading_local.a.execute("SELECT test(1,2)").next()))
sys.stdout.flush()

# This should not clean out the statement cache
# This has shown different behaviour on different machines/cpythons
# Uncomment this and see if the log statement above is preserved
