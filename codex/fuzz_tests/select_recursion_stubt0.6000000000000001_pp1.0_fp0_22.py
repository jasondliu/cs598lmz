import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    class D:
        def fileno(self):
            a.append(1)
            return 1

    select.select([F()], [], [], 0)
    select.select([D()], [], [], 0)
    assert a == [1]
