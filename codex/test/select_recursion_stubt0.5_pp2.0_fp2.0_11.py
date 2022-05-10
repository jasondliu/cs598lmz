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

    f()
    assert a == [1]


def test_select_closed_fd():
    import os
    import socket
    import select

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    sock.listen(1)
    r, w, x = select.select([sock], [], [], 0)
    assert r == [sock]
    sock.close()
    r, w, x = select.select([sock], [], [], 0)
    assert r == []
    # on Windows, socket.close() doesn't close the file descriptor
    # immediately, so we need to manually do it
    os.closerange(sock.fileno(), sock.fileno())
    r, w, x = select.select([sock], [], [], 0)
    assert r == []


