import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on collectable objects.
gc.collect()
# Test gc.collect() on uncollectable objects.
gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
# Test gc.collect() on uncollectable objects.
gc.collect()
gc.set_debug(0)

# Test weakrefs.
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()
gc.set_debug(0)

# Test cyclic trash.
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on collectable objects.
gc.collect()
# Test gc.collect() on uncollectable objects.
gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
# Test gc.collect() on uncollectable objects.
gc.collect()
gc.set_debug(0)

# Test weakrefs.
gc.set_debug(gc.DEBUG_
