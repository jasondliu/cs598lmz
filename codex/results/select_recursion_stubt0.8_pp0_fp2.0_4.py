import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    test_select_mutated()
    for i in range(4):
        a.append(i)
        r, w, x = select.select([F()], [F()], [F()], 0.1)
        assert len(r) == 1
        assert len(w) == 1
        assert len(x) == 1
