import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def f(x):
        return x

    assert select.select([f(1)], a, [], []) == ([0], [], [])
    a.append(F())
    assert select.select([f(1)], a, [], []) == ([], [], [])
    assert select.select([f(1)], a, [], []) == ([], [], [])
