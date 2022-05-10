import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

        def close(self):
            del a[:]

        def read(self):
            a.append(1)
            return 42
    select.select([F()], [], [])
    a.append(2)
    assert a == [1, 2]
