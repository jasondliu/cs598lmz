import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
collectables = gc.collect()
print 'Unreachable objects:', collectables
print 'Remaining Garbage:', gc.garbage
print

import gc
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
# Test gc.collect()
collectables = gc.collect()
# print 'Unreachable objects:', collectables
# print 'Remaining Garbage:', gc.garbage
print

import gc
gc.set_debug(gc.DEBUG_STATS)
gc.collect()
print

import gc
gc.set_debug(gc.DEBUG_LEAK)
# Test gc.collect()
collectables = gc.collect()
# print 'Unreachable objects:', collectables
# print 'Remaining Garbage:', gc.garbage
print
