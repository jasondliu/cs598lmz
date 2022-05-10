import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    def g():
        a.append(2)
        test_select_mutated()
        select.select([F()], [], [])
    a.append(1)
    g()
    raise ValueError

try:
    test_select_mutated()
except ValueError:
    pass
