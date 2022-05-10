import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    def f():
        a.append(F())

    f()
    select.select([a[0]], [], [])
