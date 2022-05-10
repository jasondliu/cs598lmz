import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    select.select([F()], [], [])

def test_select_fd_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_fd_mutated()
            return a.pop()
    select.select([F()], [], [], timeout=1)

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return a.pop()
    select.poll().register(F())

def test_poll_fd_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_fd_mutated()
            return a.pop()
    select.poll().register(F(), 1)

def test_epoll_mutated():
    a = []

    class F:
        def fileno(self):
            test_epoll_mutated()
            return a.pop()
    select.epoll().register(F
