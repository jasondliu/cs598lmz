import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.create_function


def pyfunc(func):
    def wrapped(*args):
        print("Wrapped func:")
        print(" ", args)
        return func(*args)
    return wrapped


class CreateFunctionTests(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.cur = self.con.cursor()
        self.cur.execute("create table test(x,y)")
        self.cur.execute("insert into test(x,y) values ('foo', 'bar')")
        self.cur.execute("insert into test(x,y) values ('baz', 'bax')")
        self.con.create_function("pyfunc", 1, pyfunc)

    def tearDown(self):
        self.cur.close()
        self.con.close()

    def CheckPyFunc(self):
        self.cur.execute("select pyfunc(x) from test")
        self.assertEqual(self.cur.fetchall(), [("foo",),
