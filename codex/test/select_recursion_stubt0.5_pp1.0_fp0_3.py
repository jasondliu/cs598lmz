import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def g():
        a.append(1)
        a.append(1)
        a.append(1)
        select.select([F()], [], [])

    g()
    assert a == [1, 1, 1]
