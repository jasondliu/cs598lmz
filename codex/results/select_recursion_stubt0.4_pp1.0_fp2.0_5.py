import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f():
        a.append(1)
        return [F()]

    r = select.select(f(), [], [])
    assert a == [1, 1]
    assert r == ([], [], [])
