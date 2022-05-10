import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    try:
        r, w, x = select.select(a, a, a)
    except ValueError:
        return
    assert False
