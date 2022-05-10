import codecs
codecs.register_error('strict', codecs.lookup_error('replace'))


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        _, self.db_fd = tempfile.mkstemp()
        from daimaduan import app
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + self.db_fd
        app.config['SQLALCHEMY_ECHO'] = False
        self.app = app.test_client()
        db.init_app(app)
        db.create_all()
        self.db = db

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_fd)


class TestCase(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)
        self.paste = Paste(title='test-title', content='test-content', author_id=None, language='text')
        self
