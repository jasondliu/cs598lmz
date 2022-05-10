import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    select.select(a, a, a)

def test_select_large_fd():
    a = []

    class F:
        def fileno(self):
            return sys.maxsize

    a.append(F())
    select.select(a, a, a)

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return -1

    a.append(F())
    select.select(a, a, a)

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(r)
    os.close(w)
    select.select([r], [w], [])

def test_select_closed_socket():
    s = socket.socket()
    s.close()
    select.select([s], [s], [s])

def test_select_closed_file():
    f = open(__file__, 'rb')
    f.close()

