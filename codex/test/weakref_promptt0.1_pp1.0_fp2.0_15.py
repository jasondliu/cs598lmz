import weakref
# Test weakref.ref()

class Foo(object):
    pass

def test_weakref_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    del f
    assert r() is None

def test_weakref_ref_callback():
    f = Foo()
    l = []
    def callback(r):
        l.append(r)
    r = weakref.ref(f, callback)
    assert r() is f
    del f
    assert r() is None
    assert l == [r]

def test_weakref_ref_callback_exception():
    f = Foo()
    l = []
    def callback(r):
        l.append(r)
        raise ValueError
    r = weakref.ref(f, callback)
    assert r() is f
    del f
    assert r() is None
    assert l == [r]

def test_weakref_ref_callback_exception_2():
    f = Foo()
    l = []
