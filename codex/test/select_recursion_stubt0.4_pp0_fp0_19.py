import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())
    a.append(f.fileno())
    try:
        select.select([f], [], [])
    except IndexError:
        pass
    else:
        raise Exception("didn't raise IndexError")

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [], 0)
    except OSError as e:
        assert e.errno == errno.EBADF
    else:
        raise Exception("didn't raise OSError")

def test_select_closed_socket():
    s = socket.socket()
    s.close()
    try:
        select.select([s], [], [], 0)
    except OSError as e:
        assert e.errno == errno.EBADF
    else:
        raise Exception("didn't raise OSError")

