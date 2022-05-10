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

if __name__ == '__main__':
    try:
        dll = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    except OSError:
        pass
    else:
        cb = sqlite3.set_authorizer(my_cb)
        assert not cb

        cb = sqlite3.set_authorizer()
        assert cb == my_cb

        db = sqlite3.connect(DB_URI, uri=True)

        db.execute("create table test(id integer primary key, name varchar)")
        db.commit()

        db.execute("insert into test(name) values (?)", ("test",))
        db.commit()

        for row in db.execute("select test(1, 2), id, name from test"):
            assert row[0] == 1
            assert row[1] == 1
            assert row[2] == "test"

        db.close()

        assert my_threading_local.a.closed

        print("ok")
