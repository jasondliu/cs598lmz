import weakref
# Test weakref.ref()

class Foo(object):
    pass

def test_ref():
    f = Foo()
    r = weakref.ref(f)
    assert r() is f
    del f
    assert r() is None

def test_ref_callable():
    f = Foo()
    r = weakref.ref(f, lambda x: None)
    assert r() is f
    del f
    assert r() is None

def test_ref_callable_exception():
    f = Foo()
    def fn(x):
        raise Exception
    r = weakref.ref(f, fn)
    assert r() is f
    del f
    assert r() is None

def test_ref_callable_exception_2():
    f = Foo()
    def fn(x):
        raise Exception
    r = weakref.ref(f, fn)
    assert r() is f
    del f
    assert r() is None

def test_ref_callable_exception_3():
    f = Foo()
