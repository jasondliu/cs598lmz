import weakref
# Test weakref.ref(x);
# Test weakref.ref(x, callback);

class C:
    pass

class D:
    pass

def callback(r):
    print "callback called with", r

def test_basic():
    # Test weakref.ref(x);
    o = C()
    r = weakref.ref(o)
    assert r() is o
    assert r() is o
    o2 = C()
    r2 = weakref.ref(o2)
    assert r2() is o2
    assert r2() is o2
    del o, o2
    assert r() is None
    assert r2() is None

    # Test weakref.ref(x, callback);
    o = D()
    r = weakref.ref(o, callback)
    assert r() is o
    assert r() is o
    del o
    assert r() is None

def test_callback_exception():
    # Test that if the callback function raises an exception, all is well.
    def badcallback(r):
        raise ValueError
   
