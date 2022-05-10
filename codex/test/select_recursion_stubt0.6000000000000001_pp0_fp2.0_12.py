import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    r = select.select([F()], a, a, 0)
    assert r == ([], [], [])


def test_select_mutated_2():
    a = []
    b = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    r = select.select([F()], b, b, 0)
    assert r == ([], [], [])


def test_select_mutated_3():
    a = []
    b = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    r = select.select(a, b, b, 0)
    assert r == ([], [], [])


def test_select_mutated_4():
    a = []
    b = []

    class F:
        def fileno(self):
            a.append(1)
            return 1

    r = select.select(a, [F()], b, 0)
