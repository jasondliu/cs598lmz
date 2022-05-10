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

class Test_getters(unittest.TestCase):
    def setUp(self):
        self.dbdir = tempfile.mkdtemp()
        self.db_filename = os.path.join(self.dbdir, 'a.db')
        self.db = sqlite3.connect(self.db_filename)
        self.db.execute('create table tbl (a TEXT)')
        self.db.execute('insert into tbl (a) values (?)', ('test',))
        self.db.commit()
        del self.db

    def tearDown(self):
        if os.path.isfile(self.db_filename):
            os.unlink(self.db_filename)
        os.rmdir(self.dbdir)

    def test_setters(self):
        con = sqlite3.connect(self.db_filename)
        con.enable_load_extension(True)
        fn = con.execute('select sqlite_version()').fetchone()[0]
        self.assertTrue(sqlite3._
