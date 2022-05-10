import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()

    class F2:
        def fileno(self):
            global a
            a = []
            return 5
    f2 = F2()

    a.append(f)
    select.select([f, f2], [], [], 5)
    global a
    a = None

def test_select_cannot_mutate_epoll():
    import select
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))

    poller = select.poll()
    poller.register(s, 1)

    def die():
        poller.poll()
    s.close()
    die()

def test_select_not_mutated_epoll():
    import select
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))

    poller
