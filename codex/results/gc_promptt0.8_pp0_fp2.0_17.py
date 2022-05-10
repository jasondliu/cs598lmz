import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() at the start of the program.
gc.collect()

# Test gc.collect() at the end of the program.
gc.set_finalizer(obj, finalize_obj)
obj = C()
obj.x = 1
del obj
gc.collect()

# Test gc.garbage
print gc.garbage

# Test gc.get_referents()
print gc.get_referents('abc')
print gc.get_referents(None)

# Test gc.get_referrers()
print gc.get_referrers(None)

# Test gc.get_objects()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
print gc.get_objects()

# Test gc.is_tracked()
gc.set_debug(0)
obj2 = gc.get_objects()[0]
assert gc.is_tracked(obj2) == 0

# Test gc.is_finalized()
assert gc.is_finalized(obj)

