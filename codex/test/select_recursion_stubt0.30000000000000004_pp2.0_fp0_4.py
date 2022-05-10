import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)
        select.select([F()], [], [])
        a.append(2)

    try:
        f()
    except RuntimeError:
        pass
    assert a == [1, 2]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 0

    def f():
        a.append(1)
        select.select([F()], [], [], 1)
        a.append(2)

    try:
        f()
    except RuntimeError:
        pass
    assert a == [1, 2]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return 0

    def f():
        a.append(1)
        select.select([F()], [], [], 1, 1)
        a.append(2)

