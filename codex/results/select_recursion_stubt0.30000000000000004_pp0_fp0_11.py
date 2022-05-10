import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)
    assert a == []

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

    select.select([F()], a, a, 0)
    assert a == [1]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            a.append(1)
            return 0

    select.select([F()], a, a, 0)
    assert a == [1]
