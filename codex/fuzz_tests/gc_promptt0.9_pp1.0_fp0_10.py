import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect.  It returns the number of objects it collects.
assert gc.collect() == 0
# assert gc.collect() == gc.collect() == 0
# Test gc.collect() with some uncollectable objects.
l = []
l.append(l)
l.append(weakref.ref(l))
l.append(gc)
l.append(gc.garbage)
i1 = id(l)
i2 = id(l[1])
i3 = id(l[2])
i4 = id(l[3])
del l # should have 4 refs + 1 (from gc.garbage)
assert i1 in repr(gc.garbage)
# assert gc.collect() == gc.collect() == 1
assert i1 not in repr(gc.garbage)
assert i2 not in repr(gc.garbage)
assert i3 not in repr(gc.garbage)
assert i4 not in repr(gc.garbage)

# issue22991: check that the garbage collector can deal with
# dictproxy, dictview and weakproxy objects
