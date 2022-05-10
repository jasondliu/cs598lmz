import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print(gc.collect())
print(gc.garbage)

# Test gc.get_objects()
print(len(gc.get_objects()))

# Test gc.get_count()
print(gc.get_count())

# Test gc.get_referrers()
print(len(gc.get_referrers(gc.get_objects()[0])))

# Test gc.get_referents()
print(len(gc.get_referents(gc.get_objects()[0])))

# Test gc.is_tracked()
print(gc.is_tracked('123'))
print(gc.is_tracked(123))

# Test gc.set_threshold()
print(gc.get_threshold())
gc.set_threshold(1, 2, 3)
print(gc.get_threshold())

# Test gc.disable() and gc.enable()
gc.disable()
print(gc.isenabled())
gc.enable()
print(
