import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    a.append(a[0])

    select.select(a, [], [])

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.pop()
            return 1

    a.append(F())
    a.append(a[0])

    select.select(a, [], [])

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    a.append(F())
    a.append(a[0])

    select.select(a, [], [])
