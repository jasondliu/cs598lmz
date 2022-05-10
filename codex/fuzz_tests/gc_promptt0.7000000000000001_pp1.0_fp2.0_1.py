import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.get_referrers():
l1 = []
l2 = [l1]
l3 = [l2]
l4 = [l1, l2, l3]
w4 = weakref.ref(l4)
l4 = None
gc.collect()
# after gc.collect(), l4 is no longer alive, but the reference to l4 is
# still alive
print gc.get_referrers(l1)
print w4()
# l1 is alive, l2 is alive, l3 is alive, but l4 is dead

# Test gc.get_referents():
print gc.get_referents(l1)
# l1 is alive, l2 is alive, but l3 is dead

del l1, l2, l3, w4
gc.collect()
print gc.collect()
