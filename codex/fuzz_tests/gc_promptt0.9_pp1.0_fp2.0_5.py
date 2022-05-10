import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect does not crash Python
weakref.ref(gc.collect())
