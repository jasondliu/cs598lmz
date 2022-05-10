import weakref
# Test weakref.ref, weakref.WeakKeyDictionary, and weakref.WeakValueDictionary

class C(object):
    pass

def f():
    ref = weakref.ref(C)
    # the instance is still there, the reference should be too
    assert ref() is not None
    return True

def n():
    ref = weakref.ref(C)
    # the instance is still there, the reference should be too
    assert ref() is not None
    # but if you delete the instance, the reference should disappear
    del C
    assert ref() is None
    return True

def test_weakref_ref():
    f()
    assert n()

def test_weakref_WeakKeyDictionary():
    d = weakref.WeakKeyDictionary()
    c1 = C()
    c2 = C()
    d[c1] = 42
    d[c2] = 99
    assert (c1, 42) in d.items()
    assert (c2, 99) in d.items()
    del c1
    assert (c2, 99) in
