import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with unreachable objects (Bug #1719)
wr = weakref.ref(gc.collect())
wr()
gc.get_referents(gc.collect())
