import weakref
# Test weakref.ref and weakref.proxy

def test_ref():
    class Foo:
        pass

    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    assert r.__call__() is f
    assert r() is f
    f = None
    assert r() is None

def test_proxy():
    class Foo:
        pass

    f = Foo()
    p = weakref.proxy(f)
    assert p is f
    assert p.__repr__() == "<weakproxy object at 0x%x; to 'Foo' at 0x%x>" % (id(p), id(f))
    assert p.__str__() == "<weakproxy object at 0x%x; to 'Foo' at 0x%x>" % (id(p), id(f))
    f = None
    raises(ReferenceError, repr, p)
    raises(ReferenceError, str, p)

def test_proxy_subclass():
    class Foo:
        pass
    class Bar(Foo):
        pass

