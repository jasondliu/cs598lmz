import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    a.append(F())
    select.select([a[0]], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            test_select_mutated2()
            return len(a)

    a.append(F())
    select.select([], [a[0]], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            test_select_mutated3()
            return len(a)

    a.append(F())
    select.select([], [], [a[0]])
