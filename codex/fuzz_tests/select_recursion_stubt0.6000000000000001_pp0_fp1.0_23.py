import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    assert select.select([F(), F()], [], [], 0) == ([], [], [])

class TestSelect:
    def test_select(self):
        import _socket
        s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 0))
        s.listen(1)
        s.setblocking(0)

        rfd, wfd, xfd = select.select([s], [], [], 0.1)

        assert rfd == []
        assert wfd == []
        assert xfd == []

    def test_error(self):
        import _socket
        s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 0))
        s.listen(1)
        s.setblocking(0)

        try:
            select.select([s], [s], [s], 0.1)

