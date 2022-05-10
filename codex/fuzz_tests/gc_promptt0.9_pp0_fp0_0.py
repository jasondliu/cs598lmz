import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(), which normally gets called in between
# each test run.
gc.collect()
gc.set_debug(gc.DEBUG_SAVEALL)
w = weakref.ref(str)
print "uncollectable:", len(gc.garbage)
gc.collect()
print "collectable:", len(gc.garbage)
del w
gc.garbage[:] = []
gc.collect()
print "collectable:", len(gc.garbage)
gc.garbage[:] = []
gc.set_debug(gc.DEBUG_SAVEALL)
gc.collect()
print "collectable:", len(gc.garbage)
