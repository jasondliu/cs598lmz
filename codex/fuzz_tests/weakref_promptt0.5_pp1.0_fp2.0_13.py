import weakref
# Test weakref.ref(x)
def test_ref_basic():
    class A:
        pass
    a = A()
    r = weakref.ref(a)
    assert r() is a
    assert r is not None
    assert bool(r) is True
    assert not r is None


# Test weakref.ref(x, f)
def test_ref_callback():
    class A:
        pass

    L = []

    def f(wr):
        L.append(wr)

    a = A()
    r = weakref.ref(a, f)
    assert r() is a
    assert L == []
    del a
    support.gc_collect()
    assert L == [r]
    assert r() is None


# Test weakref.proxy(x)
def test_proxy_basic():
    class A:
        pass
    a = A()
    p = weakref.proxy(a)
    assert p is a
    assert p.__class__ is A
    assert p.__doc__ is __doc__

    # Check that the hash is the
