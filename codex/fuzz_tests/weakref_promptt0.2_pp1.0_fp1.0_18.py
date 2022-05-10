import weakref
# Test weakref.ref()

class Foo:
    pass

def test_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    del f
    assert r() is None

# Test weakref.proxy()

def test_proxy():
    f = Foo()
    p = weakref.proxy(f)
    assert p is f
    del f
    raises(ReferenceError, "p.foo")

# Test weakref.getweakrefcount()

def test_getweakrefcount():
    f = Foo()
    assert weakref.getweakrefcount(f) == 0
    r = weakref.ref(f)
    assert weakref.getweakrefcount(f) == 1
    p = weakref.proxy(f)
    assert weakref.getweakrefcount(f) == 2
    del r, p
    assert weakref.getweakrefcount(f) == 0

# Test weakref.getweakrefs()

def test_getweakrefs():
    f = Foo()
    assert weakref
