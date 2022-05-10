import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], [], [])
    a.append(1)
    assert a == [1]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([F()], [], [])
    a.append(1)
    assert a == [1]

def test_select_mutated3():
    a = []

    class F:
        def fileno(self):
            return 0

    select.select([F()], [], [])
    a.append(1)
    assert a == [1]
