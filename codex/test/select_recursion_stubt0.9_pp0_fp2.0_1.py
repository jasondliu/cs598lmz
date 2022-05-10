import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            b.remove()
            return 1

    b = []
    a.append(F())
    a.append(2)

    sel
