import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())

    try:
        select.select(a, [], [])
    except ValueError:
        pass

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [], 0)
    except ValueError:
        pass
    else:
        raise ValueError("select.select should raise ValueError for closed fd")
    os.close(r)

def test_select_closed_socket():
    s = socket.socket()
    s.close()
    try:
        select.select([s], [], [], 0)
    except ValueError:
        pass
    else:
        raise ValueError("select.select should raise ValueError for closed fd")

def test_select_closed_socket_pair():
    s = socket.socketpair()
    s[0].close()
