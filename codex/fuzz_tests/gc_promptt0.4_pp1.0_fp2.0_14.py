import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage
gc.collect()
print len(gc.garbage)

# Test gc.is_tracked()
print gc.is_tracked(1)
print gc.is_tracked(gc.garbage[0])
print gc.is_tracked(gc.garbage[0].__class__)
print gc.is_tracked(gc.garbage[0].__class__.__bases__)
print gc.is_tracked(gc.garbage[0].__class__.__bases__[0])
print gc.is_tracked(gc.garbage[0].__class__.__bases__[0].__bases__)
print gc.is_tracked(gc.garbage[0].__class__.__bases__[0].__bases__[0])

# Test gc.get_referrers()
print gc.get_referrers(1)
print gc.get_referrers(gc.garbage[0])
print gc.get
