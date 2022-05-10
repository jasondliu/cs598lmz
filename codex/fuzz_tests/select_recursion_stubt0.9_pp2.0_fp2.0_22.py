import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    a.append(F())
    select.select(a, a, a, 1)

def test_select_closed():
    a = []
    a.append(1234)
    # should not crash
    select.select(a, a, a)
