import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_bad_fd():
    try:
        select.select([5], [], [])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"


def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return a.pop()

    select.poll()

def test_poll_bad_fd():
    try:
        select.poll([5], [], [])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"


def test_epoll_mutated():
    a = []

    class F:
        def fileno(self):
            test_epoll_mutated()
            return a.pop()

    select.epoll()

def test_epoll_bad_fd():
    try:
        select.epoll([5], [], [])
    except
