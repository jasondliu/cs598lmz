import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(w)
    for i in range(1000):
        select.select([r], [], [], 0)

def test_select_closed_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 80))
    s.close()
    for i in range(1000):
        select.select([s], [], [], 0)

def test_select_closed_socket_pair():
    s = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM)
    s[0].close()
    for i in range(1000):
        select.select([s[1]], [], [], 0)

def test_select_closed_pipe_pair():
    r, w = os.pipe()
    os.close(w)
    for i in
