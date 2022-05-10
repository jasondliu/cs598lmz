import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    f = F()
    select.select([f], [], [])
    assert a == [1]
    select.select([f], [], [])
    assert a == [1, 1]
