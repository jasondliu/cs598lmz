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

#
# Now we have a callback that references a connection.  This should fail
#
sqlite3.sqlite_set_authorizer(my_cb)

assert sqlite3.complete_statement("create table test (q INT);")

sqlite3.sqlite_set_authorizer(None)

#
# Now we have a callback that references a connection.  This should fail
#
sqlite3.sqlite_set_authorizer(my_cb)

assert sqlite3.complete_statement("create table test2 (q INT);")

sqlite3.sqlite_set_authorizer(None)

# Now we have a callback that references a connection and then closes it
# This should succeed
sqlite3.sqlite_set_authorizer(my_cb2)

assert sqlite3.complete_statement("create table test2 (q INT);")

sqlite3.sqlite_set_authorizer(None)

# Now we have
