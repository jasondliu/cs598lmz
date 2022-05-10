import weakref
# Test weakref.ref

class C:
    pass

def test_basic():
    o = C()
    r = weakref.ref(o)
    assert r() is o
    assert r() is not None
    del o
    assert r() is None

def test_callback():
    callback_ran = False
    def callback(r):
        nonlocal callback_ran
        callback_ran = True
    o = C()
    r = weakref.ref(o, callback)
    assert r() is o
    assert r() is not None
    del o
    assert r() is None
    assert callback_ran

def test_callback_exception():
    def callback(r):
        raise Exception
    o = C()
    r = weakref.ref(o, callback)
    assert r() is o
    assert r() is not None
    del o
    assert r() is None

def test_hash():
    o = C()
    r = weakref.ref(o)
    assert hash(r) == hash(o)
    assert hash(r) == hash
