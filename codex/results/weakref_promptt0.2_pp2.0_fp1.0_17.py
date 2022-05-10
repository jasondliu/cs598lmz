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
    def bad(x):
        raise ValueError
    r = weakref.ref(f, bad)
    assert r() is f
    del f
    assert r() is None

def test_ref_callable_exception2():
    f = Foo()
    def bad(x):
        raise ValueError
    r = weakref.ref(f, bad)
    raises(ValueError, "del f")
    assert r() is None

def test_ref_callable_exception3():
    f = Foo()
    def bad(x):
