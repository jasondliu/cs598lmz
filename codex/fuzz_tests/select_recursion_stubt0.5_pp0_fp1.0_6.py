import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

        def __del__(self):
            a.append(1)

    f = F()
    try:
        select.select([f], [], [])
    except ValueError:
        pass
    assert a == [1]

def test_select_closed_fd():
    class F:
        def fileno(self):
            return -1

    f = F()
    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_select_closed_pipe():
    import os
    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [])
    except ValueError:
        pass
    os.close(r)

def test_select_closed_socket():
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('www.pypy.org', 80))
    sock.close()
    try:
        select
