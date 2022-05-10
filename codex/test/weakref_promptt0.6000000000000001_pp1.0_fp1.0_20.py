import weakref
# Test weakref.ref()
assert isinstance(weakref.ref(object()), weakref.ReferenceType)

def test_acquire_release():
    # Acquire and release a weak reference
    o = object()
    r = weakref.ref(o)
    assert r() is o
    del o
    assert r() is None

def test_callback():
    # Test callback
    L = []
    def callback(r):
        L.append(1)
    o = object()
    r = weakref.ref(o, callback)
    assert r() is o
    del o
    assert len(L) == 1
    assert L[0] == 1
    assert r() is None

def test_callback_exception():
    # Test callback with exception
    L = []
    def callback(r):
        L.append(1)
        raise Exception
    o = object()
    r = weakref.ref(o, callback)
    assert r() is o
    del o
    assert len(L) == 1
    assert L[0] == 1
    assert r
