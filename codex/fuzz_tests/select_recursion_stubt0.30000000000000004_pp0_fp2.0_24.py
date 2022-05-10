import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return len(a)

    select.select([F()], [], [])

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return len(a)

    select.select([F()], [], [], 0.1)

def test_select_mutated_4():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return len(a)

    select.select([F()], [], [], 0.1, 0.1)

def test_select_mutated_5():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return len(a)

    select.
