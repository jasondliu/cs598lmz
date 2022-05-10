import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 4

    a.append(F())
    a.append(None)
    try:
        select.select(a, [], [])
    except ValueError:
        pass

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 4

    a.append(F())
    a.append(None)
    x = F()
    a.append(x)
    os.close(x.fileno())
    try:
        select.select(a, [], [])
    except ValueError:
        pass

def test_select_badfd():
    a = []

    class F:
        def fileno(self):
            return 4

        def close(self):
            raise IOError(errno.EBADF, "bad fd")

    a.append(F())
    a.append(None)
    try:
        select.select(a, [], [])
    except ValueError:
        pass

