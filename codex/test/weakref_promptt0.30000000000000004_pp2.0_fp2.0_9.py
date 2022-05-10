import weakref
# Test weakref.ref()

class Foo:
    pass

def bar():
    pass

class TestWeakref:

    def test_basic(self):
        f = Foo()
        p = weakref.ref(f)
        assert p() is f
        assert p() is not None
        del f
        assert p() is None

    def test_callable(self):
        f = Foo()
        p = weakref.ref(f, bar)
        assert p() is f
        assert p() is not None
        del f
        assert p() is None

    def test_proxy(self):
        f = Foo()
        p = weakref.proxy(f)
        assert p is f
        assert p is not None
        del f
        raises(ReferenceError, "p.foo")

    def test_proxy_callable(self):
        f = Foo()
        p = weakref.proxy(f, bar)
        assert p is f
        assert p is not None
        del f
        raises(ReferenceError, "p.foo")

