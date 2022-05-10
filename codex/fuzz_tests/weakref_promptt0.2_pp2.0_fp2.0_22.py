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

def test_ref_callable():
    f = Foo()
    r = weakref.ref(f, lambda x: None)
    assert r() is f
    del f
    assert r() is None

def test_ref_type():
    f = Foo()
    r = weakref.ref(f)
    assert type(r) is weakref.ref
    del f
    assert type(r) is weakref.ref

def test_proxy():
    f = Foo()
    p = weakref.proxy(f)
    assert p is f
    del f
    raises(ReferenceError, "p.attr")

def test_proxy_type():
    f = Foo()
    p = weakref.proxy(f)
    assert type(p) is weakref.ProxyType
    del f
    assert type(p) is weakref.
