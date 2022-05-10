import weakref
# Test weakref.ref() and weakref.proxy()

class C(object):
    pass

def test_ref():
    c = C()
    r = weakref.ref(c)
    assert r() is c
    assert r() is not None
    del c
    assert r() is None

def test_proxy():
    c = C()
    p = weakref.proxy(c)
    assert p is c
    assert p is not None
    del c
    raises(ReferenceError, "p.foo")

def test_ref_subclass():
    class MyRef(weakref.ref):
        pass
    c = C()
    r = MyRef(c)
    assert r() is c
    assert r() is not None
    del c
    assert r() is None

def test_proxy_subclass():
    class MyProxy(weakref.proxy):
        pass
    c = C()
    p = MyProxy(c)
    assert p is c
    assert p is not None
    del c
    raises(ReferenceError, "p.foo")


