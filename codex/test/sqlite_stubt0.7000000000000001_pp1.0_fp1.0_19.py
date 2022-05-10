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

lib = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

if lib.sqlite3_initialize() != 0:
    print("failed to initialize")
    print(lib.sqlite3_errcode(None), lib.sqlite3_errmsg(None))

p1 = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

p2 = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

p1.set_authorizer(my_cb)

p1.executescript("""
    create table test(a text);
    insert into test values ('a');
    select test('a', 'b');
""")

p2.executescript("""
    create table test(a text);
    insert into test values ('a');
    select test('a', 'b');
""")

print("finished")
