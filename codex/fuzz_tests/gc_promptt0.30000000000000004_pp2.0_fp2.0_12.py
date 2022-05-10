import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    pass

def do_nothing():
    pass

def test_gc_collect():
    # Test gc.collect()
    gc.collect()
    # Test gc.collect(generation)
    gc.collect(0)
    gc.collect(1)
    gc.collect(2)
    # Test gc.collect(generation, ...)
    gc.collect(0, 0)
    gc.collect(0, 1)
    gc.collect(0, 2)
    gc.collect(1, 0)
    gc.collect(1, 1)
    gc.collect(1, 2)
    gc.collect(2, 0)
    gc.collect(2, 1)
    gc.collect(2, 2)
    # Test gc.collect(generation, ..., ...)
    gc.collect(0, 0, 0)
    gc.collect(0, 0, 1)
    gc.collect(0, 0, 2
