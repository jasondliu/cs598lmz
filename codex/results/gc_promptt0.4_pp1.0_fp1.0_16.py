import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print(gc.garbage)

# Test gc.get_referrers()
a = [1, 2, 3]
b = [a, a]
print(gc.get_referrers(a))

# Test gc.get_referents()
print(gc.get_referents(a))

# Test gc.get_objects()
print(gc.get_objects())

# Test gc.get_threshold()
print(gc.get_threshold())

# Test gc.set_threshold()
gc.set_threshold(2, 3, 4)
print(gc.get_threshold())

# Test gc.get_count()
print(gc.get_count())

# Test gc.enable()
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_COLLECT
