import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print("gc.collect() =", gc.collect())

# Test gc.get_referrers()
print("gc.get_referrers(gc) =", gc.get_referrers(gc))

# Test gc.get_referents()
print("gc.get_referents(gc) =", gc.get_referents(gc))

# Test gc.get_objects()
print("gc.get_objects() =", gc.get_objects())

# Test gc.get_stats()
print("gc.get_stats() =", gc.get_stats())

# Test gc.is_tracked()
print("gc.is_tracked(gc) =", gc.is_tracked(gc))

# Test gc.set_debug()
print("gc.set_debug(gc.DEBUG_STATS) =", gc.set_debug(gc.DEBUG_STATS))

# Test gc.set_threshold()
print("gc.set_threshold(2,2
