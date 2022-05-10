import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 4

    x = select.select([], [0, 1, 2, F(), 5, 6], [])
    a.append(x)

    class F:
        def fileno(self):
            test_select_mutated()
            return 6

    x = select.select([0, 1, 2, 3, F(), 5, 6, 7], [], [])
    a.append(x)

    class F:
        def fileno(self):
            test_select_mutated()
            return 6

    x = select.select([0, 1, 2, 3, 5, F(), 6, 7], [], [])
    a.append(x)

    assert len(a) == 3
