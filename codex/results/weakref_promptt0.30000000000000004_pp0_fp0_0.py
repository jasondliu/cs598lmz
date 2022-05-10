import weakref
# Test weakref.ref()

class Foo:
    def __init__(self):
        self.a = 42

class Bar:
    def __init__(self):
        self.a = 42

def test_weakref_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r().a == 42
    del f
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r() is None
    assert r()
