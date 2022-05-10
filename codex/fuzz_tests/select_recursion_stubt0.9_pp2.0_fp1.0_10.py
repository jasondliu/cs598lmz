import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return -1

        def read(self):
            assert 2
    select.select([F()], [], [])
    assert a
