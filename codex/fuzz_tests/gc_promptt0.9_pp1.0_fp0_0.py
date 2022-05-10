import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weak reference.
class C:
    pass

wr = weakref.ref(C())
gc.collect()
