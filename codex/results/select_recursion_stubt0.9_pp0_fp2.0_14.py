import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    r = select.select([F()], [F()], [], 0.0)
    assert r == ([], [], []), r
    a.append(1)
    r = select.select([F()], [F()], [], 0.0)
    assert r == ([], [], []), r
    a.append(2)
    try:
        r = select.select([F()], [F()], [], 0.0)
    except IndexError:
        pass
    else:
        assert False, "expected an IndexError, got %s" % (r,)
    r = select.select([F()], [F()], [], 0.0)
    assert r == ([], [], []), r
    a.append(3)
    r = select.select([F()], [F()], [], 0.0)
    assert r == ([], [], []), r

def test_select_error():
    class F:
        def fileno(self):
            raise ValueError
    raises(ValueError, select
