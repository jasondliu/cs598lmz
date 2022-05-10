import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Create a weakref
class A:
    pass
a = A()
wra = weakref.ref(a)
# Create a cycle
a.b = [a]
del a
gc.collect()
# Check the weakref
wra()

# Test gc.get_referrers()
gc.get_referrers(wra)

# Test gc.get_referents()
gc.get_referents([a])

# Test gc.get_objects()
len(gc.get_objects())

# Test gc.garbage
gc.garbage

# Test gc.get_count()
gc.get_count()

# Test gc.get_stats()
gc.get_stats()

# Test gc.set_threshold()
gc.set_threshold()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.enable()
gc.enable()

# Test gc.disable()
gc.disable()

# Test g
