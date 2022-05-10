import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 123
    a.append(F())

    try:
        select.select([a[0]], [], [])
    except ValueError:
        pass

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return 123
    a.append(F())

    try:
        select.poll()
    except ValueError:
        pass

def test_epoll_mutated():
    a = []

    class F:
        def fileno(self):
            test_epoll_mutated()
            return 123
    a.append(F())

    try:
        select.epoll()
    except ValueError:
        pass

def test_kqueue_mutated():
    a = []

    class F:
        def fileno(self):
            test_kqueue_mutated()
            return 123
    a.append(F())

    try:
        select.kqueue()
    except ValueError:
        pass

def test_
