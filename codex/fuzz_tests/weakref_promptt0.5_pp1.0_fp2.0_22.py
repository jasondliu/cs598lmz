import weakref
# Test weakref.ref() and weakref.proxy()

import weakref

class C:
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
    assert p.__class__ is C
    assert p.__dict__ is c.__dict__
    del c
    raises(ReferenceError, "p.foo")

def test_proxy_hash():
    c = C()
    p = weakref.proxy(c)
    assert hash(p) == hash(c)
    c.foo = 1
    assert hash(p) == hash(c)
    del c
    raises(ReferenceError, "hash(p)")

def test_proxy_str():
    c = C()
    p = weakref.proxy(c)
    assert str(p) == str(c)
    c
