import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

        def read(self):
            a.append(1)
            return None

    select.select([F()], [], [])
    assert a == [1]
