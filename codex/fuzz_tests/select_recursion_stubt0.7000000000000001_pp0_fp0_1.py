import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)

    r, w, x = select.select([f], [f], [f], 0.0)
    assert r == [f]
    assert w == [f]
    assert x == [f]

    r, w, x = select.select([f], [f], [f], 0.0)
    assert r == [f]
    assert w == [f]
    assert x == [f]

    r, w, x = select.select([f], [f], [f], 0.0)
    assert r == [f]
    assert w == [f]
    assert x == [f]

    r, w, x = select.select([f], [f], [f], 0.0)
    assert r == [f]
    assert w == [f]
    assert x == [f]

class TestStr:
    def __str__(self):
        return '42'

def test_str():
    r, w, x = select.select([TestStr
