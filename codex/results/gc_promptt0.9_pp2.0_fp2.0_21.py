import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() again
print gc.collect()
print 'unreachable objects', gc.garbage
