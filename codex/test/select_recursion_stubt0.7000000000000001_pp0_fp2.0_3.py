import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(None)
            return 3

    select.select([F()], [], [])
    a.append(None)

    assert a == [None, None]

def test_select_mutated2():
    a = []

    class F:
        def fileno(self):
            a.append(None)
            return 3

    select.select([F()], [], [])
    a.append(None)

    assert a == [None, None]
