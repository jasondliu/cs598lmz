import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return -1000

    f = F()
    r = range(10)
    try:
        select.select([f], r, r)
    except ValueError:
        pass
    assert a == [1]


def test_select_closed():
    # Test that fd's are closed if not returned in the result sets.
    class F:
        def fileno(self):
            return -1

        def close(self):
            test_select_closed.seen = True

    test_select_closed.seen = False
    f = F()
    select.select([f], [], [])
    assert test_select_closed.seen

    test_select_closed.seen = False
    select.select([], [f], [])
    assert test_select_closed.seen

    test_select_closed.seen = False
    select.select([], [], [f])
    assert test_select_closed.seen


