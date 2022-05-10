import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def test_gc_collect():
    a = Foo()
    a.foo = a
    b = Foo()
    b.foo = b
    c = Foo()
    c.foo = c
    del a, b, c
    gc.collect()
    assert gc.collect() == 0

# Test gc.garbage

def test_gc_garbage():
    # This test relies on the current implementation detail that
    # uncollectable objects are appended to gc.garbage.  It would be
    # better to check gc.garbage contents more directly.

    class A:
        pass
    a = A()
    a.a = a
    gc.collect()
    assert len(gc.garbage) == 1
    del a
    gc.collect()
    assert len(gc.garbage) == 0

# Test gc.get_objects()

def test_gc_get_objects():
    # gc.get_objects() is not guaranteed to return every object in
    #
