import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test checks that the collect routine can be used from Python
# and that it works.

import gc

print gc.collect()

# Test gc.garbage
#
# This test checks that gc.garbage contains objects that cannot be
# collected.  It does not check that gc.garbage is the only list of
# such objects.

import gc

# Define a class which is not tracked by the GC
class NoGC:
    def __del__(self):
        pass

# Create an instance which will show up in gc.garbage
x = NoGC()

# Make sure the instance is tracked by the GC
del x

# Collect, so that the instance ends up in gc.garbage
gc.collect()

# Check that the object is in gc.garbage
if gc.garbage:
    if gc.garbage[0].__class__ is NoGC:
        print 'ok'
    else:
        print 'garbage[0] is not a NoGC object'
else:
   
