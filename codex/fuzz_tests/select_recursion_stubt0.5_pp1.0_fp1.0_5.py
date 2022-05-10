import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    class F2:
        def fileno(self):
            a.append(1)
            return 2

    try:
        select.select([F()], [], [], 1)
    except ValueError:
        pass
    assert a == []
    try:
        select.select([F2()], [], [], 1)
    except ValueError:
        pass
    assert a == [1]
