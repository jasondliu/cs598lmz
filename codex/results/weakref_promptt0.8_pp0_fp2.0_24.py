import weakref
# Test weakref.ref()
class TestWeakref_ref:
    def test_basic(self):
        class Foo:
            pass
        a = Foo()
        b = weakref.ref(a)
        c = weakref.ref(a, None)
        assert b is c
        #
        # Test assignment to class
        #
        class Foo:
            pass
        Foo.a = weakref.ref(Foo, None)

    def test_callable(self):
        class Foo:
            pass
        a = Foo()
        c = weakref.ref(a, None)
        assert c() is a

    def test_invalid(self):
        raises(TypeError, weakref.ref, 1)


class TestWeakref:
    class Foo:
        pass

    def test_basic(self):
        a = self.Foo()
        b = weakref.ref(a)
        c = weakref.ref(a)
        assert b is c

    def test_getweakrefcount(self):
        a = self.Foo()
        b = weakref
