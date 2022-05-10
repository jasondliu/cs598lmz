import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print(gc.garbage)
# Test weak references
gc.collect()
print(gc.garbage)

# Test reference cycles
gc.collect()
print(gc.garbage)

# Test gc.get_referents()
gc.collect()
print(gc.garbage)

gc.set_debug(0)
gc.collect()
print(gc.garbage)

# Test gc.get_referrers()
gc.set_debug(gc.DEBUG_STATS)
gc.collect()
print(gc.get_count())
gc.collect()
print(gc.get_count())
print(gc.get_stats())

# Test gc.get_objects()
gc.set_debug(gc.DEBUG_LEAK)
gc.collect()
print(gc.get_count())
print(gc.get_stats())
gc.collect()
print(gc.get_count())
print(gc.get_stats())

# Test gc.set_debug()
gc.set_debug(gc.
