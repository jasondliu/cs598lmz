import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except IndexError:
        pass
    else:
        assert False, "IndexError not raised"

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return len(a)

    f = F()
    a.append(f)
    try:
        select.select([f], [], [], 1)
    except IndexError:
        pass
    else:
        assert False, "IndexError not raised"

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return len(a)

    f = F()
    a.append(f)
    try:
        select.select([f], [], [], 1, 1)
    except IndexError:
        pass
    else
