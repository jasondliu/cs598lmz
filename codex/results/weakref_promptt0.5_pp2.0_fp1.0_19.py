import weakref
# Test weakref.ref.__init__(obj)
# Test that the ref is created, and that the object is callable


class C:

    def __init__(self, arg=None):
        self.arg = arg

    def __call__(self):
        return self.arg


def test_basic():
    c = C()
    r = weakref.ref(c)
    assert r() is c
    assert r()() is None
    c = C(10)
    assert r() is c
    assert r()() == 10
    del c
    assert r()() == 10
    assert r()() == 10
    import gc
    gc.collect()
    assert r()() == 10
    assert r()() == 10


def test_subclass():

    class D(C):
        pass
    c = D()
    r = weakref.ref(c)
    assert r() is c
    assert r()() is None
    c = D(10)
    assert r() is c
    assert r()() == 10
    del c
    assert r()
