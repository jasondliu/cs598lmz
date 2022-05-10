import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 3
    a.append(F())

    b = select.select([], a, [])
    assert b[1] == a
