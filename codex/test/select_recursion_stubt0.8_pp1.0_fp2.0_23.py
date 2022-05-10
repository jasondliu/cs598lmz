import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def f(self):
            a.append(1)

    select.select([F()], [], [], 4)
    assert a == [1]
