import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    else:
        assert False, "select.select didn't raise ValueError"

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0

    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    else:
        assert False, "select.select didn't raise ValueError"

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.pop(0)
            return 0

    a.append(F())
    try:
        select.select([], [], a, 0)
    except ValueError:
        pass
    else:
        assert False, "select.select didn't raise ValueError"

