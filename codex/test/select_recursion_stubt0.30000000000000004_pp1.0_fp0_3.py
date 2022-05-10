import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return len(a)

    select.select([F()], [], [])

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

    select.select([F()], [], [])

def test_select_closed_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

    select.select([F()], [], [])

def test_select_closed_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return len(a)

    select.select([F()], [], [])

