import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            del a[:]
            return 0

    select.select([F()], a, a, 0)

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.append(5)
            return 0

    select.select([F()], a, a, 0)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 0

    select.select([F()], a, a, 0)

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            a[:] = [1, 2, 3]
            return 0

    select.select([F()], a, a, 0)

def test_select_mutated6():
