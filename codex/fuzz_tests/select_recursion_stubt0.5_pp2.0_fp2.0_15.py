import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        try:
            select.select([F()], [], [])
        except RuntimeError:
            a.append(1)

    f()
    f()
    assert a == [1, 1]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 0

        def fileno(self):
            test_select_mutated2()
            return 0

    def f():
        try:
            select.select([], [F()], [])
        except RuntimeError:
            a.append(1)

    f()
    f()
    assert a == [1, 1]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return 0

        def fileno(self):
            test_select_
