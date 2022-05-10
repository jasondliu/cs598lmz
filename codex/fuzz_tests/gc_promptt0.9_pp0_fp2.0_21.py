import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
a = []
a = weakref.ref(a)
del a
gc.collect(2)
gc.collect(1)
gc.collect(0)
