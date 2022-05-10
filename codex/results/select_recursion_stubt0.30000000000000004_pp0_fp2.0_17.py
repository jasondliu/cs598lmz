import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    try:
        select.select(a, [], [])
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return -1

    a.append(F())
    try:
        select.select(a, [], [])
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [], 0)
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"
    os.close(r)

def test_select_closed_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
