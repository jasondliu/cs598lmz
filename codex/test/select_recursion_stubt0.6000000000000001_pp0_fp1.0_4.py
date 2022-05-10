import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f(x):
        a.append(x)

    select.select([F()], [], [], 0)
    assert a == [0]
