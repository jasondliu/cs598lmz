import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    a.append(F())
    select.select([], [], [])

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return len(a)

    a.append(F())
    select.select([], [], [])
    a.pop()
    select.select([], [], [])

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_closed_mutated()
            return len(a)

    a.append(F())
    select.select([], [], [])
    a.pop()
    select.select([], [], [])

def test_select_closed_mutated_2():
    a = []

    class F:
        def fileno(self):
            test_select_closed_mutated_2()
            return len(a)

    a.append(F())
    select.select([], [], [])
    a.
