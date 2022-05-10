import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())

    select.select([f], [], [])


def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a.append(f.fileno())
    a.append(f.fileno())

    select.select([f], [], [])


def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a.append(f.fileno())
    a.append(f.fileno())

    select.select([f], [f], [f])


def test_select_mutated4():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a.append(f.fileno())
    a.append(f.fileno())


