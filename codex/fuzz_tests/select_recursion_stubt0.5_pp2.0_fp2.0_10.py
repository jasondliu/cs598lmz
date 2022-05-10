import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        select.select([], [], a, 1)
    except ValueError:
        pass

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(w)
    try:
        select.select([r], [], [], 0)
    except ValueError:
        pass
    os.close(r)

def test_select_closed_socket():
    s = socket.socket()
    s.close()
    try:
        select.select([s], [], [], 0)
    except ValueError:
        pass

def test_select_closed_file():
    f = open(os.devnull)
    f.close()
    try:
        select.select([f], [], [], 0)
    except ValueError:
        pass

def test_select_closed_connection():
    c = socket.socket()
    c.close()
    try:
        select.select([c], [], [], 0)
    except
