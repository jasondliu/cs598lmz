import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print(gc.garbage)

# Test gc.get_referrers()
a = []
b = [a]
c = [a, b]
del a, b
gc.collect()
print(gc.get_referrers(c))

# Test gc.get_referents()
a = []
b = [a]
c = [a, b]
del a, b
gc.collect()
print(gc.get_referents(c))

# Test gc.get_objects()
a = []
b = [a]
c = [a, b]
del a, b
gc.collect()
print(gc.get_objects())

# Test gc.get_stats()
a = []
b = [a]
c = [a, b]
del a, b
gc.collect()
print(gc.get_stats())

# Test gc.is_tracked()
a = []
b = [a]
c = [a, b]
del a, b
gc
