import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    s = select.select([], [F()], [])

    a.append(0)
    a.append(2)

test_select_mutated()
