import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0.001)

def test_select_bad_arguments():
    a = []

    try:
        select.select(a, a, a, 'hello')
    except TypeError:
        pass
    else:
        assert False, 'expected TypeError'

    try:
        select.select(1, 2, 3)
    except TypeError:
        pass
    else:
        assert False, 'expected TypeError'

    try:
        select.select()
    except TypeError:
        pass
    else:
        assert False, 'expected TypeError'

    try:
        select.select(1, 2, 3, 4, 5)
    except TypeError:
        pass
    else:
        assert False, 'expected TypeError'

def test_select_timeout():
    # Issue #3023.
    r, w, x = select.select([], [], [], 0.1)
    assert r == []
    assert w == []
    assert x == []

