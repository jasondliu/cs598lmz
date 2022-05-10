import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    l = [weakref.ref(x) for x in range(5)]
    return l

l1 = f()
l2 = f()
#print(gc.collect())
#print(gc.collect())
print(gc.collect())

# Test gc.get_referrers()
#print(gc.get_referrers(l1))

# Test gc.get_referents()
#print(gc.get_referents(l1))

# Test gc.get_objects()
#print(gc.get_objects())

# Test gc.is_tracked()
#print(gc.is_tracked(l1))

# Test gc.set_threshold()
#print(gc.get_threshold())
#gc.set_threshold(100, 10, 10)
#print(gc.get_threshold())

# Test gc.get_count()
#print(gc.get_count())

# Test gc.get_stats()
#print(gc.get
