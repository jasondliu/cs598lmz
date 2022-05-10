import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.pop()
            return 5

    f = F()

    try:
        select.select([f], [f], [f])
    except TypeError:
        pass
    else:
        assert 0, "unexpected success (1)"

    try:
        a = [f]
        select.select(a, a, a)
    except TypeError:
        pass
    else:
        assert 0, "unexpected success (2)"
