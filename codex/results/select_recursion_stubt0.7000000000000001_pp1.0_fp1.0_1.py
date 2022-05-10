import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.insert(0, f)
    try:
        sel = select.select(a, [], [])
    except ValueError:
        pass

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a[:] = []
            return 0

    f = F()
    a.insert(0, f)
    try:
        sel = select.select(a, [], [])
    except ValueError:
        pass
