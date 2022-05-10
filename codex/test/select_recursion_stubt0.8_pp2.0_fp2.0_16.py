import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 42

    r, w, e = select.select([F()], a, a)
    r, w, e = select.select(a, [F()], a)
    r, w, e = select.select(a, a, [F()])
    r, w, e = select.select([], [], [])


