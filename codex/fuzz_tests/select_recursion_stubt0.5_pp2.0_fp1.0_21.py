import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(1)
    select.select([f], [f], [f])


def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a.append(1)
    select.select([f], [f], [f])


def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_closed_mutated()
            return a.pop()

    f = F()
    a.append(1)
    select.select([f], [f], [f])


def test_select_closed_mutated_2():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    a.append(1)
    select.select([f], [f], [f])
    test_select_closed_mutated_2()



