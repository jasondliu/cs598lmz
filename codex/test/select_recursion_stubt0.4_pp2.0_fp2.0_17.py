import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            del a[:]
            return len(a)

    select.select([F()], [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a[:] = []
            return len(a)

    select.select([F()], [], [])

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a[:] = [1, 2, 3]
            return len(a)

    select.select([F()], [], [])

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

    select.select([F()], [], [])

