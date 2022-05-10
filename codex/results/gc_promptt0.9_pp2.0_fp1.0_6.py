import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
if verbose:
    print 'Before, number of collected objects:', gc.collect()
w = weakref.ref(C())
if verbose:
    print 'Before, number of collected objects:', gc.collect()
w()
gc.collect()
if verbose:
    print 'After, number of collected objects:', gc.collect()
print 'End'

# Comment out the following lines to see
# the effect without the cyclic trashcan
#print w() is w()
print w()
