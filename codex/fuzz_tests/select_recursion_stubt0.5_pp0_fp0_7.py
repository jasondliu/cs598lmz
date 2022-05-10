import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([], [], [F()])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

    select.select([], [], [F()])

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            test_select_mutated()
            return len(a)

    select.select([], [], [F()])

def test_select_closed_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            test_select_mutated()
            return len(a)

    select.select([], [F()], [])

def test_select_closed_mutated3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            test_select_
