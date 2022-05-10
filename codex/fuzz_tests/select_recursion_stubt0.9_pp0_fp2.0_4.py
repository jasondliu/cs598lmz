import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return None
        def __getattr__(self, name):
            try:
                return getattr(select, name)
            except AttributeError:
                a.append(name)
                return lambda *args, **kw: self

    f = F()
    f.select([[]], [], [])
    f.epoll_wait(1, 0)
    f.poll_wait(1, 0)
    f.devpoll_wait(1, 0)
    f.kevent(1, 0, 0, 0)
    assert a == ['select', 'select_mutated', 'select']

def test_select_mutated_epoll():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_epoll()
            return None
        def __getattr__(self, name):
            try:
                return getattr(select, name)
            except AttributeError:
                a.append(name)
                return lambda *args, **kw: self

    f = F()
    f.kqueue
