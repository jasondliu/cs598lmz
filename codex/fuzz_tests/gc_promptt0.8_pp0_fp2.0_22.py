import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() immediately after the weakref creation
gc.collect()
gc.set_debug(0)
# The weakref will now be cleared
del w
#f = w()
#print f
