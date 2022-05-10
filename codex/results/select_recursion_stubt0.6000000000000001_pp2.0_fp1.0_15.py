import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    a.append(F())
    select.select([], [], [])
    a.pop()

# test_select_mutated()

def test_sock_vs_duck():
    class F:
        def fileno(self):
            return 3
    f = F()
    try:
        select.select([f], [f], [f])
    except TypeError:
        pass
    else:
        raise AssertionError("did not raise TypeError")

    try:
        select.select([f], [f], [f], 3.14)
    except TypeError:
        pass
    else:
        raise AssertionError("did not raise TypeError")

    class S:
        def fileno(self):
            return 3
        def family(self):
            return AF_INET
        def type(self):
            return SOCK_STREAM
    s = S()

    select.select([s], [s], [s])
    select.select([s], [s], [s], 3.14
