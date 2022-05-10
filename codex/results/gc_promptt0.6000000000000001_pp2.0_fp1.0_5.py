import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable objects.
def collect_uncollectable():
    class A:
        pass
    a = A()
    wr = weakref.ref(a)
    a.attr = a
    gc.collect()
    assert wr() is a
    del a
    gc.collect()
    assert wr() is None
collect_uncollectable()
# Test gc.collect() with collectable objects.
def collect_collectable():
    class A:
        pass
    a = A()
    wr = weakref.ref(a)
    gc.collect()
    assert wr() is a
    del a
    gc.collect()
    assert wr() is None
collect_collectable()
# Test gc.collect() with collectable and uncollectable objects.
def collect_collectable_and_uncollectable():
    class A:
        pass
    a = A()
    wr = weakref.ref(a)
    a.attr = a
    gc.collect()
    assert wr() is a
    del a
    gc.collect
