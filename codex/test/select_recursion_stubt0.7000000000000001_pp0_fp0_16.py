import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    assert select.select(a, [], [], 0) == ([f], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a[:] = []
            return 0

    f = F()
    a.append(f)
    assert select.select(a, [], [], 0) == ([f], [], [])

def test_select_mutated3():
    a = []
    b = []

    class F:
        def fileno(self):
            nonlocal a
            a[:] = b
            return 0

    f = F()
    a.append(f)
    assert select.select(a, [], [], 0) == ([f], [], [])

def test_select_mutated4():
    a = []
    b = []

    class F:
        def fileno(self):
            a = b
            return 0

    f = F()

