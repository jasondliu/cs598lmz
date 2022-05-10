import weakref
# Test weakref.ref() and weakref.proxy()

class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "C(%r)" % self.x

def test_ref():
    c = C(10)
    r = weakref.ref(c)
    assert r() is c
    assert repr(r) == "C(10)"
    assert str(r) == "C(10)"
    del c
    assert r() is None
    assert repr(r) == "C(10)"
    assert str(r) == "C(10)"

def test_proxy():
    c = C(10)
    p = weakref.proxy(c)
    assert p.x == 10
    assert repr(p) == "C(10)"
    assert str(p) == "C(10)"
    del c
    raises(ReferenceError, "p.x")
    raises(ReferenceError, "repr(p)")
    raises(ReferenceError, "str(p)")

def
