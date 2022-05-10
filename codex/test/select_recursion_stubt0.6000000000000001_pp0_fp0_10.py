import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    fds = [F(), F()]
    try:
        select.select(fds, fds, fds)
    except ValueError:
        pass

def test_select_bigfd():
    # Issue #2295: select shouldn't complain about file descriptors > FD_SETSIZE
    class F:
        def fileno(self):
            return int(1e9)
    try:
        select.select([], [F()], [])
    except ValueError:
        pass

def test_select_badarg():
    # Issue #2991: select shouldn't crash when passed a non-integer
    # object as a file descriptor.
    class F:
        def fileno(self):
            return 'ham'
    try:
        select.select([F()], [], [])
    except TypeError:
        pass

