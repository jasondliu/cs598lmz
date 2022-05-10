import codecs
codecs.register_error('strict', codecs.ignore_errors)

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


class Test_db_base(TestCase):
    def test_db_base(self):
        db = DB_Base(db_name='test_db')
        self.assertTrue('test_db' in db.db_name)
        self.assertTrue(db.db_name.endswith('.db'))

        self.assertTrue(db.db_path.endswith(db.db_name))
        self.assertTrue(db.conn)
        self.assertTrue(db.cursor)
        self.assertTrue(db.close())


class Test_db_tables(TestCase):
    def test_db_tables(self):
        db = DB_Base(db_name='test_db')
        db.create_table('test_table', ['id INTEGER PRIMARY KEY', 'name TEXT', 'email TEXT'])
        self
