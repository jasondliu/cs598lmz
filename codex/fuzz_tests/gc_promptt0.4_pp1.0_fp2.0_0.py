import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a

# Test weakrefs
ref = weakref.ref(a)
del a
gc.collect()
print ref() is None

# Test gc.garbage
gc.garbage.append(b)
del b
gc.collect()
print gc.garbage

# Test gc.get_objects()
print len(gc.get_objects())

# Test gc.get_referrers()
print len(gc.get_referrers(gc))

# Test gc.get_referents()
print len(gc.get_referents(gc))

# Test gc.is_tracked()
print gc.is_tracked(gc)

# Test gc.set_threshold()
print gc.get_threshold()
gc.set_threshold(100, 10, 10)
print gc.get_threshold()

# Test gc.get
