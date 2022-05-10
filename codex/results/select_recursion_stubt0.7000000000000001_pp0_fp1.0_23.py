import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 2

    def g():
        a.append(1)
        return a.pop()

    f = F()
    assert select.select([], [f], [f], 0) == ([], [], [])
