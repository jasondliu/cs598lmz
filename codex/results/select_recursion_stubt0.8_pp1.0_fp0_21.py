import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    f = F()
    a.append(f)

    try:
        select.select(a,a,a)
    except ValueError:
        pass

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a[:] = []
            return -1

    f = F()
    a.append(f)

    try:
        select.select(a,a,a)
    except ValueError:
        pass
