import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
def test_gc_collect():
    # Test gc.collect
    class C:
        pass

    c = C()
    wr = weakref.ref(c)
    c.foo = c
    c.bar = c
    gc.collect()
    assert wr() is c

    c = C()
    wr = weakref.ref(c)
    c.foo = c
    c.bar = c
    c.foo = None
    gc.collect()
    assert wr() is None

    c = C()
    wr = weakref.ref(c)
    c.foo = c
    c.bar = c
    c.foo = None
    c = None
    gc.collect()
    assert wr() is None

    c = C()
    wr = weakref.ref(c)
    c.foo = c
    c.bar = c
    c = None
    gc.collect()
    assert wr() is None

    c = C()
    wr = weakref.ref(c)
    c.foo = c
    c
