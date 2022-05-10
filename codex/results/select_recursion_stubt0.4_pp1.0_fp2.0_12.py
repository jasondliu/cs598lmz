import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    f = F()
    a.append(f)
    try:
        select.select([f], [f], [f], 0)
    except ValueError:
        pass

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [], 0)
    except ValueError:
        pass

def test_select_closed_socket():
    s = socket.socket()
    s.close()
    try:
        select.select([s], [], [], 0)
    except ValueError:
        pass
