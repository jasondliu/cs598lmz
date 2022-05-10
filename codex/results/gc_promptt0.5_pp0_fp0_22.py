import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = [1, 2, 3]
a = []
gc.collect()
# Test gc.get_objects()
gc.collect()
a = [1, 2, 3]
b = [4, 5, 6]
gc.collect()
objects = gc.get_objects()
print len(objects)
print objects[:10]
# Test gc.get_referents()
gc.collect()
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
gc.collect()
referents = gc.get_referents(a)
print len(referents)
print referents
# Test gc.get_referrers()
gc.collect()
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
gc.collect()
referrers = gc.get_referrers(a)
print len(referrers)
print referrers
# Test gc.get_count()
gc.collect()
