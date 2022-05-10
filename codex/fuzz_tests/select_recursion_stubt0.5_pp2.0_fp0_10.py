import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    a.append(F())

    select.select(a, [], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return 1
    a.append(F())

    select.select(a, [], [])

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a[:] = []
            return 1
    a.append(F())

    select.select(a, [], [])

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a[:] = [None]
            return 1
    a.append(F())

    select.select(a, [], [])

def test_select_mutated_5():
    class F:
        def fileno(self):
            return 1
    a = [F(), F()]

    del a[1
