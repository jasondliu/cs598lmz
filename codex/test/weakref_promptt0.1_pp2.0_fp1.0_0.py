import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    pass

def test_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    del f
    assert r() is None

def test_proxy():
    f = Foo()
    p = weakref.proxy(f)
    assert p is f
    del f
    raises(ReferenceError, "p.attr")

def test_callbacks():
    # Test weakref callbacks
    f = Foo()
    l = []
    def callback(arg):
        l.append(arg)
    r = weakref.ref(f, callback)
    assert r() is f
    del f
    assert l == [r]
    del l[:]
    f = Foo()
    r = weakref.ref(f, callback)
    assert r() is f
    del r
    assert l == [None]
    del l[:]
    f = Foo()
    r = weakref.ref(f, callback)
    assert r() is f
   
