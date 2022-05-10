import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    f = F()
    a.append(f)

    for ignore in select.select([f], [], [], 0):
        pass

def test_select_mutated2():
    # This used to segfault in CPython
    a = []
    a.append(a)

    for ignore in select.select(a, [], [], 0):
        pass

def test_select_fds():
    # check that select() takes file descriptors, not fileno() return values
    class F:
        def fileno(self):
            return sys.maxsize+1

    f = F()
    try:
        select.select([f], [], [])
    except ValueError:
        pass
    else:
        assert False, "select.select([f], [], []) must raise ValueError"
