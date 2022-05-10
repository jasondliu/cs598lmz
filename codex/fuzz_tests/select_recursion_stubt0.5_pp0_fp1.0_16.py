import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return a.pop()

    select.select([F()], [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return a.pop()

    select.select([F()], [], [], 1)
