import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    a.append(F())
    select.select([], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

    a.append(F())
    select.select([], [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            del a[:]
            return len(a)

    a.append(F())
    select.select([], [], [])

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            del a[:]
            return len(a)

    a.append(F())
    select.select([], [], [])

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            a[:] = []
            return len(a)


