import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on an object with a weakref.
weakref.ref().collect()
# Test gc.collect() on an object with a cycle.
gc.collect()
x = []
x.append(x)
gc.collect()
