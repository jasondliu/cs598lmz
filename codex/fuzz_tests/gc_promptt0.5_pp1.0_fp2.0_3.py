import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# This test is currently known to fail with Python versions 2.3 and 2.4,
# because of a bug in the garbage collector:  gc.collect() does not
# collect weakrefs.  This was fixed in Python 2.5.

# The test is skipped if the weakref module is not available.

import sys
import weakref

if not hasattr(sys, 'gettotalrefcount'):
    raise ImportError('test requires sys.gettotalrefcount()')

# Create a cycle, and suppress the finalizer on one of the objects
# involved in the cycle.

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
wr = weakref.ref(b, lambda x: x)
del b

# Collect and check that a and wr are still alive.

gc.collect()
if wr() is None:
    raise Exception("weak reference should not have died")
if wr() is not a:
    raise Exception("weak reference should refer to a")

# Check that wr is still alive
