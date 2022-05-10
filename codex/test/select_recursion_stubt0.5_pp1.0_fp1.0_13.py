import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    select.select([], [], a)

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return 0

    a.append(F())
    select.poll().poll(0, a)

def test_epoll_mutated():
    a = []

    class F:
        def fileno(self):
            test_epoll_mutated()
            return 0

    a.append(F())
    select.epoll().poll(0, a)

def test_kqueue_mutated():
    a = []

    class F:
        def fileno(self):
            test_kqueue_mutated()
            return 0

    a.append(F())
    select.kqueue().control(a, 0, 0)

def test_select_closed_fd():
    r, w = os.pipe()
