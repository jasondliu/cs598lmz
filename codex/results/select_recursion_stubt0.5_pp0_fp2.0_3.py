import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 42

    select.select([F()], [], [], 0)


def test_select_closed():
    import select, socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        # UDP sockets are not supported
        return
    s.bind(('localhost', 0))
    s.close()

    try:
        select.select([s], [], [], 0)
    except ValueError:
        pass
    else:
        raise ValueError("select.select([closed_socket], [], [], 0) didn't raise")


def test_select_interrupted():
    import select, socket, errno
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    r, w, x = select.select([s], [], [], 0)
    assert not r and not w and not x
    s
