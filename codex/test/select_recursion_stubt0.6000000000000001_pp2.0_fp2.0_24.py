import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 5

    a.append(F())

    try:
        select.select(a, [], [])
    except ValueError as e:
        assert "I/O operation on closed file" in repr(e)
    else:
        assert False, "did not raise"

def test_select_closed_fd():
    import socket
    s = socket.socket()
    s.close()
    try:
        select.select([s], [], [])
    except ValueError as e:
        assert "I/O operation on closed file" in repr(e)
    else:
        assert False, "did not raise"
