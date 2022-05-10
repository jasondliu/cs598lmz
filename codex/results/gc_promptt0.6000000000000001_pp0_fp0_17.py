import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
w = weakref.ref(gc.collect())
del w
gc.collect()
# Test gc.garbage
gc.garbage.append(gc.garbage)
gc.collect()
print gc.garbage
del gc.garbage[:]
gc.collect()
# Test gc.get_debug()
print gc.get_debug()
gc.set_debug(0)
print gc.get_debug()
gc.set_debug(gc.DEBUG_LEAK)
print gc.get_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.get_objects(), gc.get_referrers(), gc.get_referents()
a = []
b = [a]
a.append(b)
print gc.get_objects()
print gc.get_referrers(b)
print gc.get_referents(b)
# Test gc.is_tracked()
print gc.is_tracked(b)
a = []
print gc.
