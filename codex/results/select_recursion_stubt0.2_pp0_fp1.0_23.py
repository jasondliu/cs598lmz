import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_closed_socket():
    s = socket.socket()
    s.close()
    try:
        select.select([s], [], [])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_closed_file():
    f = open(test_support.TESTFN, "w")
    f.close()
    try:
        select.select([f], [], [])
    except ValueError:
        pass
    else:
