import weakref
# Test weakref.ref(a) and weakref.proxy(a)

class Foo(object):
    pass

foo = Foo()

def test_ref(a):
    w = weakref.ref(a)
    x = w()
    assert x is a
    assert w() is a
    del a
    assert w() is None

test_ref(foo)
test_ref(Foo())


def test_proxy(a):
    w = weakref.proxy(a)
    assert w is a
    del a
    raises(ReferenceError, "w.x")
    raises(ReferenceError, "w.__class__")

test_proxy(foo)
test_proxy(Foo())

class Foo(object):
    def __init__(self, x):
        self.x = x

foo = Foo(42)

def test_ref(a):
    w = weakref.ref(a)
    assert w().x == 42
    del a
    assert w() is None

test_ref(foo)
test_ref(Foo(42))
