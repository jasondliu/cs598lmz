import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)
        return F()

    select.select([f()], [], [])
    assert a == [1]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return 0

    def f():
        a.append(1)
        return F()

    select.select([f()], [], [], 0.1)
    assert a == [1]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return 0

    def f():
        a.append(1)
        return F()

    select.select([], [f()], [])
    assert a == [1]

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return 0


