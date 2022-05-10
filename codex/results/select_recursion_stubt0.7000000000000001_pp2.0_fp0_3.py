import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    a.append(F())
    s = select.select([], a, [], 0)
    del a[:]
    s = select.select([], a, [], 0)
