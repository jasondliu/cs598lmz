import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return fd

    f = F()
    a = [f]
    fd = f.fileno()

    select.select(a, a, a, 1)
