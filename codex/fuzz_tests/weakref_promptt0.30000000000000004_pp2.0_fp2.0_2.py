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
    r = weakref.ref(f, lambda _: None)
    assert r() is f
    del f
    assert r() is None

def test_ref_callable_exception():
    f = Foo()
    def bar(x):
        raise ValueError
    raises(ValueError, weakref.ref, f, bar)
    assert f is not None

def test_ref_callable_exception_2():
    f = Foo()
    def bar(x):
        raise ValueError
    raises(ValueError, weakref.ref, f, bar)
    assert f is not None

def test_ref_callable_exception_3():
    f = Foo()
    def bar(x):
        raise ValueError
    raises(ValueError, weakref
