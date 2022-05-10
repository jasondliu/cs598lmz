import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print(gc.garbage)

# Test gc.get_referrers()
a = []
b = [a]
c = [a, b]
print(gc.get_referrers(a))
print(gc.get_referrers(b))
print(gc.get_referrers(c))

# Test gc.get_referents()
print(gc.get_referents(a))
print(gc.get_referents(b))
print(gc.get_referents(c))

# Test gc.get_objects()
print(gc.get_objects())

# Test gc.is_tracked()
print(gc.is_tracked(a))
print(gc.is_tracked(b))
print(gc.is_tracked(c))

# Test gc.is_finalized()
print(gc.is_finalized(a))
print(gc.is_finalized(b))
print(gc.is_finalized(c))

#
