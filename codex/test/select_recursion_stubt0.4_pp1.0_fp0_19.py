import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def close(self):
            pass

    select.select([F()], [], [])
    raise Exception("Didn't crash")

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return len(a)
        def close(self):
            pass

    p = select.poll()
    p.register(F(), select.POLLIN)
    p.poll()
    raise Exception("Didn't crash")

def test_epoll_mutated():
    a = []

    class F:
        def fileno(self):
            test_epoll_mutated()
            return len(a)
        def close(self):
            pass

    p = select.epoll()
    p.register(F(), select.EPOLLIN)
    p.poll()
    raise Exception("Didn't crash")

def test_kqueue_mutated():
    a = []

