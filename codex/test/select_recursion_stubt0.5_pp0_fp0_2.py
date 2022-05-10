import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append("fileno")
            return self.fd

        def read(self):
            a.append("read")
            return ""

    f = F()
    f.fd = 12
    select.select([f], [], [], 0)
    assert a == ["fileno", "read"]

def test_select_closed():
    import select
    import socket
    import errno

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.close()
    assert s.fileno() == -1
    try:
        select.select([s], [], [], 0)
    except select.error as e:
        assert e.args[0] == errno.EBADF
    else:
        assert False, "select() on a closed socket did not raise an exception"

class TestSelect:
    def test_select(self):
        import select
        import socket

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
