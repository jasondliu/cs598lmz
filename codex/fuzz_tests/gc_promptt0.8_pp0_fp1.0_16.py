import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print 'About to call gc.collect()'
print 'Collectable objects:', gc.collect()
print 'Uncollectable objects:', gc.collect(1)
print 'About to call gc.collect() again'
print 'Collectable objects:', gc.collect()
print 'Uncollectable objects:', gc.collect(1)
