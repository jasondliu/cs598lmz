import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.collect(generation)
gc.collect(2)
# Test gc.garbage
print(gc.garbage)

# Test gc.get_count()
print(gc.get_count())

# Test gc.get_debug()
print(gc.get_debug())

# Test gc.get_referrers()
print(gc.get_referrers(None))

# Test gc.get_threshold()
print(gc.get_threshold())

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_SAVEALL)

# Test gc.set_threshold()
gc.set_threshold(1, 2, 3)

# Test gc.is_tracked()
print(gc.is_tracked(None))

# Test gc.is_finalized()
print(gc.is_finalized(None))

# Test gc.set_finalizer()
gc.set_finalizer(None, lambda x: None)

