import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    select.select([F()], [], [])
    assert a

def test_select_bad_fd():
    r, w, x = select.select([1], [], [])
    assert r == [1]
    r, w, x = select.select([], [1], [])
    assert w == [1]
    r, w, x = select.select([], [], [1])
    assert x == [1]

    raises(ValueError, select.select, [1, 2], [], [])
    raises(ValueError, select.select, [], [1, 2], [])
    raises(ValueError, select.select, [], [], [1, 2])

    raises(ValueError, select.select, [1, 2], [1, 2], [1, 2])
    raises(ValueError, select.select, [1, 2], [1, 2], [])
    raises(ValueError, select.select, [1, 2], [], [1, 2])
