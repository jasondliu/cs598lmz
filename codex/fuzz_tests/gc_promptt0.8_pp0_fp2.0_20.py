import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() always returns 0.
gc.collect()
gc.collect()
gc.collect()

class Test_weakref:
    def test___new__(self):
        class Foo:
            pass
        foo = Foo()
        r = weakref.__new__(weakref.ref, foo)
        assert isinstance(r, weakref.ref)

    def test_call(self):
        class Foo:
            pass
        foo = Foo()
        r = weakref.ref(foo)
        assert r() is foo
        del foo
        gc.collect()
        assert r() is None

    def test_hash_equality(self):
        class Foo:
            pass
        foo = Foo()
        foo2 = Foo()

        xref = weakref.ref(foo)
        yref = weakref.ref(foo)
        xref2 = weakref.ref(foo2)

        assert xref.hash == yref.hash
        assert xref is not yref
        assert xref2.hash != xref.hash
        assert xref2 != xref
