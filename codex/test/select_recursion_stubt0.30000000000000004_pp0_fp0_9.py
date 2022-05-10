import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return 1

    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    else:
        assert False, "select() didn't raise ValueError"

