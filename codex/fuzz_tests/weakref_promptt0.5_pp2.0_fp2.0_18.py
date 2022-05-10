import weakref
# Test weakref.ref() on a callable object.
class C(object):
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return self.x + y

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

def test_callable():
    c = C(1)
    c2 = C(2)
    ref = weakref.ref(c)
    ref2 = weakref.ref(c2)
    assert ref() is c
    assert ref2() is c2
    del c
    assert ref() is None
    assert ref2() is c2
    del c2
    assert ref() is None
    assert ref2() is None

def test_builtin():
    ref = weakref.ref(f)
    assert ref() is f
    del f
    assert ref() is None

def test_builtin_method():
    class X(object):
        def __init__(self, x):
           
