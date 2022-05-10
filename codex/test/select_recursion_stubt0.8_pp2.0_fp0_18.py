import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    l = [F()]
    l.extend(range(10))
    a.extend(range(11))

    select.select(l, l[:1], l[:2])

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return a.pop()

    l = [F()]
    l.extend(range(10))
    a.extend(range(11))

    poll = select.poll()
    for f in l:
        poll.register(f, select.POLLIN)

    try:
        poll.poll()
    except IndexError:
        pass

def test_epoll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return a.pop()

    l = [F()]
    l.extend(range(10))
    a.extend(range(11))

    ep
