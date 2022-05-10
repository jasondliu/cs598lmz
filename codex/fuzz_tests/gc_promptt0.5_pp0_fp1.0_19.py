import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print("after collect:", gc.collect())

# Test gc.get_debug()
print("gc.get_debug():", gc.get_debug())

# Test gc.get_count()
print("gc.get_count():", gc.get_count())

# Test gc.get_objects()
print("gc.get_objects():", len(gc.get_objects()))

# Test gc.get_referrers()
print("gc.get_referrers():", gc.get_referrers(gc))

# Test gc.get_referents()
print("gc.get_referents():", gc.get_referents(gc))

# Test gc.is_tracked()
print("gc.is_tracked():", gc.is_tracked(gc))

# Test gc.is_finalized()
print("gc.is_finalized():", gc.is_finalized(gc))

# Test gc.set_debug()
gc
