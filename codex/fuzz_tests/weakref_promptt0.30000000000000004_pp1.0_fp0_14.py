import weakref
# Test weakref.ref() and weakref.proxy()

class Foo(object):
    pass

def test_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    assert r is not f
    assert r() is not f
    assert r() is not None
    del f
    assert r() is None
    assert r() is None

def test_proxy():
    f = Foo()
    p = weakref.proxy(f)
    assert p is f
    assert p is not f
    assert p is not None
    del f
    raises(ReferenceError, "p.x")
    raises(ReferenceError, "p.x")

def test_ref_call():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    raises(TypeError, "r()")

def test_proxy_call():
    f = Foo()
    p = weakref.proxy(f)
    assert p is f
    raises(TypeError, "p()")

def test_ref_
