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

libc = ctypes.CDLL(ctypes.util.find_library('c'))

libc.setenv("SQLITE_GET_DELETE_THIS", "1", 1)

db = sqlite3.connect(DB_URI)

db.set_progress_handler(my_cb, 100)

db.execute(
    'CREATE TABLE foo (id INTEGER PRIMARY KEY);'
)
db.commit()

def fn():
    for i in range(100):
        db.execute(
            'INSERT INTO foo VALUES (null);'
        )
    db.commit()

libc.usleep(100 * 1000)

t = threading.Thread(target=fn)
t.start()
t.join()

libc.usleep(100 * 1000)

delattr(my_threading_local, 'a')

libc.usleep(100 * 1000)
