import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    try:
        select.select([], [], a)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0

    f = F()
    a.append(f)
    try:
        select.select([], [], a)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0

    f = F()
    a.append(f)
    try:
        select.select([], [], a)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

def test_select_mutated4():
    a = []


