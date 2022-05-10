import weakref
# Test weakref.ref(x)
# Test weakref.proxy(x)
# Test weakref.getweakrefcount(x)
# Test weakref.getweakrefs(x)
# Test weakref.ref(x)

def test_weakref_ref():
    class Foo(object):
        pass

    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    assert r() is not None
    assert r() is not None
    del f
    #assert r() is None


# Test weakref.proxy(x)

def test_weakref_proxy():
    class Foo(object):
        pass

    f = Foo()
    p = weakref.proxy(f)
    assert p is f
    assert p is not None
    assert p is not None
    del f
    #assert p is None


# Test weakref.getweakrefcount(x)

def test_weakref_getweakrefcount():
    class Foo(object):
        pass

    f = Foo()
    assert weakref.getweakrefcount(f
