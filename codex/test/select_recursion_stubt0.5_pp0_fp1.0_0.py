import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    a.append(3)
    a.append(5)
    r, w, x = select.select([F()], [F()], [F()], 0.0)
    assert r == w == x == []

def test_select_large_lists():
    # Issue #11507: select() shouldn't crash with large lists.
    # The test is a bit racy, but the chance of select() returning
    # successfully for such a large list is pretty much nil.
    a = []
    for i in range(100000):
        a.append(i)
    try:
        select.select(a, a, a, 0.0)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

