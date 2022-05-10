import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
l = [1, 2, 3, 4, 5]
w = weakref.ref(l)
print(gc.collect())
del l
print(gc.collect())
print(w())
print(gc.collect())
print(w())

# Test gc.garbage
gc.collect()
print(gc.garbage)
l = []
l.append(l)
print(gc.garbage)

print(gc.get_count())
print(gc.get_threshold())

# Test gc.get_debug()
print(gc.get_debug())
gc.set_debug(gc.DEBUG_STATS)
print(gc.get_debug())

# Test gc.get_objects()
print(len(gc.get_objects()))

# Test gc.get_referrers()
class A:
    pass
a = A()
print(gc.get_referrers(a))

# Test gc.get_referents()
print(gc.get_referents(a))

# Test gc
