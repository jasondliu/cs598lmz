import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42
        def close(self):
            a.append(1)

    try:
        select.select([F()], [], [], 0)
    except OSError:
        pass
    assert a == [1]

def test_select_closed():
    import _socket
    a = []

    class F:
        closed = False
        def fileno(self):
            return 42
        def close(self):
            a.append(1)

    try:
        select.select([F()], [], [])
    except OSError:
        pass
    assert a == [1]
    sock = _socket.socket(_socket.AF_INET, _socket.SOCK_DGRAM)
    sock.close()
    try:
        select.select([sock], [], [])
    except OSError:
        pass
    else:
        assert 0, "expected an OSError"

