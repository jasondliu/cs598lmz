import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)
        select.select([F()], [], [])

    raises(RuntimeError, f)
    assert a == []

def test_select_error():
    import errno
    class F:
        def fileno(self):
            return 0
        def close(self):
            pass
    f = F()
    def fileno():
        raise OSError(errno.EBADF, "bad file descriptor")
    f.fileno = fileno
    raises(OSError, select.select, [f], [], [])
    f.close()

class TestSelect:
    def setup_class(cls):
        cls.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.serv.bind(('localhost', 0))
        cls.serv.listen(1)
        cls.port = cls.serv.getsockname()[1]
