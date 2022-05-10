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

sqlite3.enable_shared_cache(False)
sqlite3.SQLITE_ATTR_SHARED_CACHE = 1000
sqlite3.SQLITE_THREADSAFE = 1

db = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
db.execute("CREATE TABLE test (a integer);")
db.execute("""
create trigger r1 after insert on test
begin
    update test set a=new.a where rowid=new.rowid;
end;
""")

libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.malloc(64)

db.execute("PRAGMA temp_store = MEMORY")
db.set_authorizer(lambda x,y,z,w: 1 if x == sqlite3.SQLITE_READ and y == "test" and w == "a" else None)

t1 = threading.Thread(target=my_cb, args=(db,))
t1.start()
t1.join
