import weakref
# Test weakref.ref(obj)

# Test that the weakref.ref(obj) constructor works.

def test_ref():
    class Foo:
        pass
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    assert r.__call__() is f

# Test weakref.proxy(obj)

# Test that the weakref.proxy(obj) constructor works.

def test_proxy():
    class Foo:
        pass
    f = Foo()
    p = weakref.proxy(f)
    assert p is f
    assert p.__class__ is Foo
    assert p.__dict__ is f.__dict__
    assert p.__weakref__ is f.__weakref__
    f.x = 42
    assert p.x == 42
    f.x = 43
    assert p.x == 43
    del f.x
    raises(AttributeError, "p.x")
    raises(TypeError, "p.x = 42")
    raises(TypeError, "del p.x")
