import select
# Test select.select

def test_select():
    # select.select() is not implemented yet
    raises(NotImplementedError, select.select, [], [], [])

def test_select_exception():
    raises(TypeError, select.select, [], [], [], 'foo')
    raises(TypeError, select.select, [], [], [], timeout=None)

class TestSelect:
    def setup_class(cls):
        cls.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.serv.bind(('127.0.0.1', 0))
        cls.serv.listen(5)
        cls.port = cls.serv.getsockname()[1]

    def teardown_class(cls):
        cls.serv.close()

    def test_basic(self):
        s1, addr = self.serv.accept()
        s2, addr = self.serv.accept()
        s1.send(b'xyz')
