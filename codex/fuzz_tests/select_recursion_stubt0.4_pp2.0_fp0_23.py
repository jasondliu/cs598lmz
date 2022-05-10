import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass
    else:
        assert False, "select() didn't raise RuntimeError"

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0

    a.append(F())
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass
    else:
        assert False, "select() didn't raise RuntimeError"

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return 0

    a.append(F())
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass
    else:
        assert False, "select() didn't raise RuntimeError"

def test_select_mutated_4():
    a =
