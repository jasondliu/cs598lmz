import select
# Test select.select

def test_select():
    r, w, e = select.select([], [], [], 1)
    assert r == w == e == []

# Test select.poll

class TestPoll:

    def setup_class(cls):
        cls.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.serv.bind(('127.0.0.1', 0))
        cls.serv.listen(5)
        cls.port = cls.serv.getsockname()[1]
        cls.cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def teardown_class(cls):
        cls.serv.close()
        cls.cli.close()

    def test_poll(self):
        p = select.poll()
        p.register(self.serv, select.POLLIN)
        p.register(self.cli, select.POLLIN)
        r = p.poll(1)
        assert r
