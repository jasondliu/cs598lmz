import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print(gc.collect())
print(gc.garbage)

# Test gc.get_referrers()
a = [1, 2, 3]
b = [a, a]
print(gc.get_referrers(a))
print(gc.get_referrers(b))

# Test gc.get_referents()
print(gc.get_referents(a))
print(gc.get_referents(b))

# Test gc.get_objects()
print(gc.get_objects())

# Test gc.get_stats()
print(gc.get_stats())

# Test gc.is_tracked()
print(gc.is_tracked(a))
print(gc.is_tracked(b))

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
print(gc.get_stats())

# Test gc.set_threshold()
print(gc.get_threshold())
gc.set_th
