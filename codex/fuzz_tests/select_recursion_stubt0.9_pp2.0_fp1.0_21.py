import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    w, r, e = select.select([], a, [], 0)

def test_select_mutated_rev():
    a = []

    class F:
        def fileno(self):
            test_select_mutated_rev()
            return 1

    a.append(F())
    r, w, e = select.select([], a, [], 0)
