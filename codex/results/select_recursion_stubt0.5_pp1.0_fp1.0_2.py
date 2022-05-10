import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    a.append(F())
    a.append(F())

    r, w, x = select.select([], a, [])
    assert len(r) == 0
    assert len(w) == 3
    assert len(x) == 0
