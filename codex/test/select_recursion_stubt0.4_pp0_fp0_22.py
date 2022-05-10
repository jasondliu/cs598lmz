import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    with pytest.raises(ValueError):
        select.select([F()], [], [])

def test_select_closed_fd():
    # Issue #12457: select() should not crash when given a closed file
    # descriptor.
    a = []

    class F:
        def fileno(self):
            a.pop()
            raise ValueError

    with pytest.raises(ValueError):
        select.select([F()], [], [])

def test_select_closed_pipe():
    # Issue #12457: select() should not crash when given a closed pipe
    # descriptor.
    import os
    r, w = os.pipe()
    os.close(w)
    with pytest.raises(ValueError):
        select.select([r], [], [])

def test_select_closed_socket():
    # Issue #12457: select() should not crash when given a closed socket
    # descriptor.
    import socket
    s = socket.socket()
    s.close()
