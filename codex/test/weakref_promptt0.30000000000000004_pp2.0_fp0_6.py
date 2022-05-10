import weakref
# Test weakref.ref() and weakref.proxy()

class Foo(object):
    pass

class Bar(object):
    pass

def test_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    assert r.__call__() is f
    f = None
    assert r() is None
    assert r.__call__() is None
    raises(TypeError, r, 1)
    raises(TypeError, r.__call__, 1)
    raises(TypeError, weakref.ref, Foo)
    raises(TypeError, weakref.ref, 1)
    raises(TypeError, weakref.ref, "hello")
    raises(TypeError, weakref.ref, 1.0)
    raises(TypeError, weakref.ref, [])
    raises(TypeError, weakref.ref, ())
    raises(TypeError, weakref.ref, {})
    raises(TypeError, weakref.ref, object)
    raises(TypeError, weakref.ref, object())
