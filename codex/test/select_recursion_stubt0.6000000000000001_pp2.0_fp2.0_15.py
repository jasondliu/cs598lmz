import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    select.select([f], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return a.pop()

    f = F()
    select.select([f], [], [])

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    select.poll()
    select.poll().register(f)

def test_poll_closed():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return a.pop()

    f = F()
    select.poll()
    select.poll().register(f)

def test_epoll_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop
