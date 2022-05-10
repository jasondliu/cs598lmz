import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())

    try:
        select.select(a, a, a)
    except RuntimeError:
        pass
    else:
        assert False, 'select() did not raise RuntimeError'
