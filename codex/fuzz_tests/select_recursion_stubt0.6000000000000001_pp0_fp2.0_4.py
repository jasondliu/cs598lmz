import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def __enter__(self):
            return self
        def __exit__(self, *args):
            a.pop()
    f = F()
    a.append(f)
    select.select([f], [f], [f])

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return len(a)
        def __enter__(self):
            return self
        def __exit__(self, *args):
            a.pop()
    f = F()
    a.append(f)
    select.poll()

def test_epoll_mutated():
    a = []

    class F:
        def fileno(self):
            test_epoll_mutated()
            return len(a)
        def __enter__(self):
            return self
        def __exit__(self, *args):
            a.pop()
    f = F()
    a.append(f)
    select
