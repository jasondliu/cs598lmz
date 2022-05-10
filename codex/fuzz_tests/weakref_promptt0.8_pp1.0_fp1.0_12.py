import weakref
# Test weakref.ref objects for truth.

def isalive(o):
    "Return whether the object is alive."
    if isinstance(o, weakref.ReferenceType):
        return o() is not None
    else:
        return True

class C(object):
    pass

def test_bound(C, C2):
    # Test __nonzero__
    c = C()
    ref = weakref.ref(c)
    c2 = C2(ref)
    if isalive(ref):
        assert c2
    c = None
    assert not c2

    # Test __len__
    c = C()
    ref = weakref.ref(c)
    c2 = C2(ref)
    if isalive(ref):
        assert len(c2) == 1
    c = None
    assert len(c2) == 0

    # Test __bool__
    c = C()
    ref = weakref.ref(c)
    c2 = C2(ref)
    if isalive(ref):
        assert bool(c2)

