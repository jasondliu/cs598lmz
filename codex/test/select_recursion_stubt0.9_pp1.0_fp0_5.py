import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[len(a) - 1]

        def executed(self):
            a.append(0)

    s = select.select([F()], [F()], [F()], None)
    assert len(a) == 3
    assert set(a) == set([0])
