import weakref
# Test weakref.ref(x)

def test_ref_new():
    # basic test of weakref.ref(x)
    class C:
        pass
    c = C()
    c.foo = "bar"
    r = weakref.ref(c)
    assert r() is c
    assert r().foo == "bar"
    assert str(r) == "<weakref at %#x; to 'C' at %#x>" % (id(r), id(c))
    assert repr(r) == "<weakref at %#x; to 'C' at %#x>" % (id(r), id(c))

def test_ref_call():
    # test calling a weakref.ref object
    class C:
        pass
    c = C()
    c.foo = "bar"
    r = weakref.ref(c)
    assert r() is c
    assert r().foo == "bar"

def test_ref_hash():
    # test hash() and comparison of weakref.ref objects
    class C:
        pass
    c = C()

