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
        select.select([f], [], [])
    except RuntimeError:
        pass

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            a.append(1)

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except RuntimeError:
        pass
    assert a == [f, 1]

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 0
        def close(self):
            a.append(1)

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except RuntimeError:
        pass
    assert a == [f, 1]

def test_select_closed_mutated2():
    a = []


