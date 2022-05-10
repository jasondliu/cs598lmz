import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without DEBUG_COLLECTABLE.
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()
gc.set_debug(gc.DEBUG_COLLECTABLE)

# Test gc.collect() with DEBUG_COLLECTABLE.
gc.collect()

# Test weakref.ref() with DEBUG_COLLECTABLE.
weakref.ref(C())
gc.collect()

# Test weakref.proxy() with DEBUG_COLLECTABLE.
weakref.proxy(C())
gc.collect()

# Test gc.get_referrers() with DEBUG_COLLECTABLE.
gc.get_referrers(C)
gc.collect()

# Test gc.get_referents() with DEBUG_COLLECTABLE.
gc.get_referents(C)
gc.collect()
