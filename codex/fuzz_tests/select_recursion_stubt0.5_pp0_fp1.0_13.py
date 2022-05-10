import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 3

    a.append(F())

    select.select(a, a, a, 1)
    assert False, "select() should have raised an error"
