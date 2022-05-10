import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    select.select([], [F()], [])
    a.append(0)
    test_select_mutated()

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return len(a)
    select.select([], [F()], [], 1)
    a.append(0)
    test_select_mutated()

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return len(a)
    select.select([F()], [], [])
    a.append(0)
    test_select_mutated()

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            test_select_mutated4()
            return len(a)
    select.select([F()], [], [], 1)
    a
