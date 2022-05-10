import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()  # mutates `a`
            return 0

    a.append(F())

    # This function should not raise any exception.
    select.select(a, a, a)
