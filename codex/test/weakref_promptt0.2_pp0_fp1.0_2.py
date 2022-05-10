import weakref
# Test weakref.ref()

class Foo(object):
    pass

def test_weakref_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    assert r() is not None
    del f
    assert r() is None

def test_weakref_ref_callable():
    f = Foo()
    r = weakref.ref(f, lambda x: None)
    assert r() is f
    assert r() is not None
    del f
    assert r() is None

def test_weakref_ref_callable_exception():
    f = Foo()
    def raise_exception(x):
        raise Exception()
    r = weakref.ref(f, raise_exception)
    assert r() is f
    assert r() is not None
    del f
    assert r() is None

# Test weakref.proxy()

def test_weakref_proxy():
    f = Foo()
    p = weakref.proxy(f)
    assert p is f
    assert p is not None
   
