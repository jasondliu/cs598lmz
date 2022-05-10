import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
print(gc.garbage)

# Test gc.get_referrers()
a = []
b = [a]
c = [b]
del a, b
gc.collect()
print(gc.get_referrers(c))

# Test gc.get_referents()
a = []
b = [a]
c = [b]
del b
gc.collect()
print(gc.get_referents(a, c))

# Test gc.get_objects()
print(gc.get_objects())

# Test gc.get_count()
print(gc.get_count())

# Test gc.get_threshold()
print(gc.get_threshold())

# Test gc.set_threshold()
print(gc.set_threshold(700, 10, 10))
print(gc.get_threshold())

# Test gc.enable()
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc
