import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    r, w, x = select.select([F()], [F()], [F()])
    assert r == []
    assert w == []
    assert x == []

def test_select_closed():
    a = []
    class F:
        def fileno(self):
            a.append(1)
            return len(a)

        def close(self):
            a.append(2)

    r, w, x = select.select([F()], [F()], [F()])
    assert r == []
    assert w == []
    assert x == []
    assert a == [1, 1, 1, 2, 2, 2]

def test_select_closed_mutated():
    a = []
    class F:
        def fileno(self):
            a.append(1)
            return len(a)

        def close(self):
            a.append(2)
            test_select_closed_mutated()

