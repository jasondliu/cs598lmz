import weakref
# Test weakref.ref() and weakref.proxy() on various objects

class C:
    pass

def f():
    pass

class D:
    def __init__(self, x=None):
        self.x = x

class E(D):
    pass

class F(D):
    def __init__(self, x=None):
        D.__init__(self, x)

def test_basic():
    o = C()
    p = weakref.proxy(o)
    assert p.__class__ is weakref.ProxyType
    assert p() is o
    assert repr(p) == "<weakproxy at %#x to %r at %#x>" % (id(p), o.__class__, id(o))
    o2 = C()
    p2 = weakref.proxy(o2)
    assert p2.__class__ is weakref.ProxyType
    assert p2() is o2
