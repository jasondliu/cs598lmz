import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print(gc.garbage)

# Test gc.get_objects()
print(len(gc.get_objects()))

# Test gc.get_referrers()
print(len(gc.get_referrers(gc)))

# Test gc.get_referents()
print(len(gc.get_referents(gc)))

# Test gc.get_threshold()
print(gc.get_threshold())

# Test gc.set_threshold()
gc.set_threshold(1, 1, 1)
print(gc.get_threshold())

# Test gc.is_tracked()
print(gc.is_tracked(gc))

# Test gc.is_finalized()
print(gc.is_finalized(gc))

# Test gc.enable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

# Test gc.disable()
gc.disable()
print(gc.isenabled())

# Test
