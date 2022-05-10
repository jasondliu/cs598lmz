import weakref
# Test weakref.ref() and weakref.proxy() with a non-weakrefable object.

class C:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

class D(C):
    def __init__(self, x):
        C.__init__(self, x)
        self.__weakref__ = None

class E(C):
    def __init__(self, x):
        C.__init__(self, x)
        self.__weakref__ = None

    def __hash__(self):
        return hash(self.x)

def test_ref():
    o = C(1)
    r = weakref.ref(o)
    assert r() is o
    assert r() == o
    assert r() != D(1)
    assert r() != E(1)

def test_proxy():
    o = C(1)
    p = weakref.proxy(o)
    assert p is o
