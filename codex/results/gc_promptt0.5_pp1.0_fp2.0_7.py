import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = [1, 2, 3]
b = [a, a, a]
del a
gc.collect()
print gc.collect()

# Test gc.garbage
gc.garbage = [1, 2, 3]
print gc.collect()
print gc.garbage

# Test gc.get_objects()
print len(gc.get_objects())

# Test gc.get_referrers()
def f():
    return gc.get_referrers(f)
print f()

# Test gc.get_referents()
a = object()
b = [a, a, a]
print gc.get_referents(b)

# Test gc.get_threshold()
print gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(2)
print gc.get_threshold()
gc.set_threshold(700, 10, 10)
print gc.get_threshold()

# Test gc.is
