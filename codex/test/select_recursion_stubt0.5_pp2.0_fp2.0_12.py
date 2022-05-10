import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    def f(x):
        a.append(x)
        return x

    select.select([F()], [], [], 1)
    a = list(map(f, a))
