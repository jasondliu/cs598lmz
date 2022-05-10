import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
# Create a cycle and verify gc can break it.
class C:
    pass
x = c = C()
c.x = x
del c, x
gc.collect()
