import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    F1, F2 = F(), F()
    a2 = select.select([F1], [], [])
    a1 = select.select([], [F2], [])
    x = (a1, a2)
    a1 = (a2, a1)
