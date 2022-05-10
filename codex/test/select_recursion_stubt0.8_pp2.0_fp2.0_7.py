import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    f = F()
    a.append(f)
    try:
        select.select(a, a, a, 1)
    except IndexError:
        pass
    else:
        assert 0, "select() did not fail"


def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1
    f = F()
    a.append(f)
    try:
        select.select(a, a, a, 1)
    except IndexError:
        pass
    else:
        assert 0, "select() did not fail"


def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a[:] = [a[0]]
            return 1
    f = F()
    a.append(f)
    try:
        select.select(a, a, a, 1)
    except IndexError:
        pass
