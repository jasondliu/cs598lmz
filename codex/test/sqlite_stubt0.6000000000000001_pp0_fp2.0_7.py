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

ctypes.CDLL(ctypes.util.find_library('sqlite3'),
            use_errno=True).sqlite3_commit_hook(
                ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb))

# Test that the test_fn function is not kept alive by the foreign function
# pointer (pysqlite bug #40)
a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
a.execute("create table test (x)")
a.execute("insert into test values (test(1, 2))")
a.commit()

# Test that the function is kept alive by the foreign function pointer
a.execute("insert into test values (test(1, 2))")

del my_threading_local.a

a.commit()

# The following commit should fail
try:
    a.commit()
except Exception:
    pass
else:
    assert False

# The following commit should work
