import weakref
# Test weakref.ref()

def f():
    return 42

class C:
    pass

def test_ref():
    o = C()
    r = weakref.ref(o)
    assert r() is o
    assert r() is not None
    assert r() is r()
    assert r() is r()
    del o
    assert r() is None
    assert r() is None
    assert r() is None

    o = f
    r = weakref.ref(o)
    assert r() is o
    assert r() is not None
    assert r() is r()
    assert r() is r()
    del o
    assert r() is None
    assert r() is None
    assert r() is None

    o = C()
    r = weakref.ref(o, lambda x: None)
    assert r() is o
    assert r() is not None
    assert r() is r()
    assert r() is r()
    del o
    assert r() is None
    assert r() is None
    assert r() is None

    o = f
   
