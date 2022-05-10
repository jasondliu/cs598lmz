import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print(gc.collect())

# Test gc.get_referrers()
a = [1, 2, 3]
print(gc.get_referrers(a))

# Test gc.get_referents()
print(gc.get_referents(a))

# Test gc.get_objects()
print(gc.get_objects())

# Test gc.is_tracked()
print(gc.is_tracked(a))

# Test gc.get_count()
print(gc.get_count())

# Test gc.get_stats()
print(gc.get_stats())

# Test gc.garbage
print(gc.garbage)

# Test gc.get_threshold()
print(gc.get_threshold())

# Test gc.set_threshold()
print(gc.set_threshold(1, 1, 1))
print(gc.get_threshold())

# Test gc.callbacks
print(gc.callbacks)

# Test gc.
