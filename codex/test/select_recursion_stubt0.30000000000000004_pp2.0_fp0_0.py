import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    select.select([F()], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return a[0]

    select.select([F()], [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return a[0]

    select.select([F()], [], [], 0.1)

def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return a[0]

    select.select([F()], [], [], 1)

def test_select_mutated5():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return a[0]

