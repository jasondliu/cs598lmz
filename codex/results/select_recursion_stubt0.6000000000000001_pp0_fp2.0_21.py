import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    a.append(F())
    try:
        select.select(a, a, a)
    except RuntimeError:
        pass
    else:
        assert 0, 'expected RuntimeError'
