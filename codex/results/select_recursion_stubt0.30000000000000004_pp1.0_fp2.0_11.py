import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    f.close = lambda: a.append(1)
    select.select([f], a, a, 0)
    assert a == [1]

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    f.close = lambda: test_select_closed_mutated()
    select.select([f], a, a, 0)

def test_select_closed_mutated2():
    a = []

    class F:
        def fileno(self):
            return 0

    f = F()
    f.close = lambda: test_select_closed_mutated2()
    select.select([f], a, a, 0)

def test_select_closed_mutated3():
    a = []


