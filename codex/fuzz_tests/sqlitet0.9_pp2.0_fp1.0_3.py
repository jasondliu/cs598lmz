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

CHILD_COUNT = 1000
try_count = 0
while 1:
    try:
        try_count += 1
        print("try_count: {}".format(try_count))

        ctypes.CDLL(ctypes.util.find_library('sqlite3'))

        lib = ctypes.CDLL('libsqlitefunctions.so')
        conn = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)
        conn.create_function('my_cb', 1, my_cb)
        conn.executescript('''
            create table testfuncs(
                id integer primary key,
                text text,
                num double,
                data blob
            );
        ''')

        for i in range(0, CHILD_COUNT):
            conn.execute('''
                insert into testfuncs (id, text, num, data)
                values (?, upper(? || ?), ? || ?.1, zeroblob(?))
            ''', [i, 'text', str(i), str
