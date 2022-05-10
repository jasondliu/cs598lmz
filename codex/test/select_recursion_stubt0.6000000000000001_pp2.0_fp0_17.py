import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    assert select.select([F()], [], [], 0) == ([], [], [])

    a = [10]
    raises(ValueError, select.select, [F()], [], [], 0)
    a = []

    assert select.select([F()], [], [], 0) == ([], [], [])

def test_select_with_strange_input():
    # select() should ignore file descriptors that are not ints (not even
    # longs)
    assert select.select([], [], [], 0) == ([], [], [])
    assert select.select([], [], [], 0, None) == ([], [], [])
    assert select.select([], [], [], 0, []) == ([], [], [])
    assert select.select([], [], [], 0, {}) == ([], [], [])
    assert select.select([], [], [], 0, "") == ([], [], [])
