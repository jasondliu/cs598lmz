import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [])
    assert a == [1]

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            test_select_closed()
            a.append(1)
        def close(self):
            a.append(2)

    select.select([F()], [], [])
    assert a == [2, 1]
