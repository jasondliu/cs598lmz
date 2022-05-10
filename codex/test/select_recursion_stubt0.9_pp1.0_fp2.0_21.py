import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 10

    def append_a():
        a.append(1)

    s = select.select([F()], [], [], 0.01)
    assert s == ([], [], []), s
    s = select.select([F()], [], [], 0.01)
    assert s == ([], [], []), s
    s = select.select([], [F()], [], 0.01)
    assert s == ([], [], []), s
    s = select.select([], [F()], [], 0.01)
    assert s == ([], [], []), s
    s = select.select([], [], [F()], 0.01)
    assert s == ([], [], []), s
    s = select.select([], [], [F()], 0.01)
    assert s == ([], [], []), s

    a = [0]

    s = select.select([], [], [], 0.01, append_a)
    assert s == ([], [], []), s
