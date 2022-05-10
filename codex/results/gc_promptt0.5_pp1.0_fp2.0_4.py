import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

a = []
b = [a]
a.append(b)

print(gc.collect())

a = []
b = [a]
a.append(b)

print(gc.collect())

# Test gc.is_tracked()
a = []
b = [a]
a.append(b)

print(gc.is_tracked(a))
print(gc.is_tracked(b))

# Test gc.get_referrers()
a = []
b = [a]
a.append(b)

print(gc.get_referrers(a))
print(gc.get_referrers(b))

# Test gc.get_referents()
a = []
b = [a]
a.append(b)

print(gc.get_referents(a))
print(gc.get_referents(b))

# Test gc.get_objects()
a = []
b = [a]
a.append(b)

