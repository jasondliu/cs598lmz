import weakref
# Test weakref.ref()
from test import test_support

class C:
    pass

def test_basic():
    c = C()
    r = weakref.ref(c)
    assert r() is c
    c2 = C()
    r2 = weakref.ref(c2)
    assert r2() is c2

    class D:
        pass
    d = D()
    rd = weakref.ref(d)
    assert rd() is d

    class E(D):
        pass
    e = E()
    re = weakref.ref(e)
    assert re() is e

class Callback:
    def __init__(self, obj):
        self.obj = obj
    def __call__(self, obj):
        self.obj = None

def test_callback():
    c = C()
    r = weakref.ref(c, Callback(c))
    assert r() is c
    del c
    test_support.gc_collect()
    assert r() is None

