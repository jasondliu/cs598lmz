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
            a.append(1)
            return len(a)

    select.select([F()], [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

    select.select([F()], [], [], 1)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

    select.select([F()], [], [], 1, 1)

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

