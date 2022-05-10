import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without a collector.
gc.collect()
# Test gc.collect() with a collector.
gc.collect(2)

# Test the debug flag.
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(0)

# Test the threshold.
gc.get_threshold()
gc.set_threshold(700)
gc.get_threshold()
gc.set_threshold(10, 10, 10)
gc.get_threshold()

# Test get_objects.
gc.get_objects()

# Test get_referrers.
gc.get_referrers(gc)

# Test get_referents.
gc.get_referents([])

# Test is_tracked.
gc.is_tracked(42)

# Test is_tracked.
gc.is_tracked("abc")

# Test is_tracked.
gc.is_tracked(gc)

# Test is_tracked.
gc.is
