import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

        def close(self):
            a.append(1)

    f = F()
    r, w, x = select.select([f], [f], [f])
    assert r == []
    assert w == []
    assert x == []
    assert a == [1]

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 1

        def close(self):
            a.append(1)

    f = F()
    f.close()
    r, w, x = select.select([f], [f], [f])
    assert r == []
    assert w == []
    assert x == []
    assert a == [1]

def test_select_closed_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_closed_mutated()

        def close(self):
            a.append(1)

    f = F()
    f.close()
    r, w, x = select.select([f], [f
