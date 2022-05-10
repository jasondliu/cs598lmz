import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        select.select([], a, [], 1)
    except ValueError:
        pass
    else:
        raise Exception("ValueError not raised")

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [], 1)
    except ValueError:
        pass
    else:
        raise Exception("ValueError not raised")

def test_select_closed_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    s.close()
    try:
        select.select([s], [], [], 1)
    except ValueError:
        pass
    else:
        raise Exception("ValueError not raised")

def test_select_closed_dup():
    s = socket.socket(socket.AF_INET, socket.SOCK_
