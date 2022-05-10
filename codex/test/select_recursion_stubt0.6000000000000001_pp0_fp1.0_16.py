import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    f = F()

    # This is supposed to raise ValueError but not crash
    select.select([], [f], [])
    assert a
