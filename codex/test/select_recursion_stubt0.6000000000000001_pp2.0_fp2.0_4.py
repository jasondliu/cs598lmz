import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self):
            a.append(1)

    select.select([F()], [], [])
    assert a == []
    assert 1 in a
