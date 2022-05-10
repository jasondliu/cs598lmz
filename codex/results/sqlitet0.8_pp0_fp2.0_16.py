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

sqlite3.enable_shared_cache(True)
sqlite3.set_authorizer(my_cb)

# This just calls sqlite3_open(file:test?mode=memory)
# And that's all
db = sqlite3.connect(DB_URI, uri=True)

db.execute('select test(6, 7)')

# This line is necessary to "use" the callback
# Otherwise the next sqlite3_open will not call
# the callback again
db.execute('select * from sqlite_master')

# So here, sqlite3_open is called in the interpreter
# and has no callback registered, so this fails.
#
# db2 = sqlite3.connect(DB_URI, uri=True)
# db2.execute('select test(6, 7)')
#
# To fix it, the next line is necessary:
sqlite3.set_authorizer(None)
db2 = sqlite3.connect(DB_URI, uri=True)
db2.execute('select test(6, 7)')

