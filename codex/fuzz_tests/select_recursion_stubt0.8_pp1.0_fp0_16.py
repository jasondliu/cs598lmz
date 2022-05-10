import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

        def close(self):
            pass

    f = F()
    a.append(f)
    r, w, x = select.select([f], [f], [f])
    assert f in r
    assert f in w
    assert f in x
    assert len(r) == 1
    assert len(w) == 1
    assert len(x) == 1
    assert r[0] is f
    assert w[0] is f
    assert x[0] is f

def test_select_closed():
    class F:
        def __init__(self):
            self.closed = False

        def fileno(self):
            return 0

        def close(self):
            self.closed = True

    f = F()
    r, w, x = select.select([f], [f], [f])
    assert not f.closed

def test_select_invalid():
    # Issue #8699: On Windows, negative file descriptors are invalid.

    class Bad(object):
        def fileno(self):
