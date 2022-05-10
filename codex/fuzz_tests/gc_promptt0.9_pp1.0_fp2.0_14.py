import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
A = gc.collect()
print(A)
# Test gc.get_count
print(gc.get_count())
# Test gc.get_stats
print(gc.get_stats())
# Test gc.debug
# Test gc.set_debug
# Test gc.get_debug
# Test gc.get_referrers
