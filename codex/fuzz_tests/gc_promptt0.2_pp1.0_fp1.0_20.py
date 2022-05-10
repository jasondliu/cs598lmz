import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test gc.get_objects()
gc.get_objects()

# Test gc.get_referrers()
gc.get_referrers(gc)

# Test gc.get_referents()
gc.get_referents(gc)

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(1000, 10, 10)
gc.get_threshold()

# Test gc.is_tracked()
gc.is_tracked(gc)

# Test gc.is_finalized()
gc.is_finalized(gc)

# Test gc.garbage
gc.garbage

# Test gc.get_count()
gc.get_count()

# Test gc.callbacks
gc.callbacks

# Test gc.DEBUG_COLLECTABLE
gc.DEBUG_COLLECTABLE

# Test gc.DEBUG_UNCOLLECTABLE
gc.DEBUG_UN
