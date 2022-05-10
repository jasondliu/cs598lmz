import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in the absence of any uncollectable objects.
gc.collect()
# Test gc.collect() in the presence of an uncollectable object.
gc.collect()

# Test gc.get_objects().
gc.get_objects()

# Test gc.get_referrers().
gc.get_referrers(gc)

# Test gc.get_referents().
gc.get_referents(gc)

# Test gc.get_threshold().
gc.get_threshold()

# Test gc.is_tracked().
gc.is_tracked(gc)

# Test gc.set_threshold().
gc.set_threshold(1, 2, 3)

# Test gc.get_count().
gc.get_count()

# Test gc.disable() and gc.enable().
gc.disable()
gc.enable()

# Test gc.isenabled().
gc.isenabled()

# Test gc.collect() with verbose=True.
gc.collect(verbose=
