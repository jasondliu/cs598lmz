import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    try:
        select.select(a, a, a, 0)
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

def test_select_large_fd():
    a = []

    class F:
        def fileno(self):
            return sys.maxsize + 1

    a.append(F())
    try:
        select.select(a, a, a, 0)
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

def test_select_negative_fd():
    a = []

    class F:
        def fileno(self):
            return -1

    a.append(F())
    try:
        select.select(a, a, a, 0)
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

def test_select_bad_fd():
    a = []

    class
