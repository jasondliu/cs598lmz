import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

        def close(self):
            self.closed = True

    test_select_mutated()
    assert a == []
    f = F()
    assert not f.closed
    a = [f]
    test_select_mutated()
    assert f.closed
    assert a == []

def test_select_multiple():
    a = []
    b = []
    c = []
    def f(l):
        def g():
            l.append(1)
        return g
    # the following fails if the "select" function is not implemented
    # correctly in the interp-level
    select.select(a, b, c, 0.0, f(a))
    select.select(a, b, c, 0.0, f(b))
    select.select(a, b, c, 0.0, f(c))
    assert a == [1]
    assert b == [1]
    assert c == [1]

def test_select_multiple_2():
    a = []
    b = []
