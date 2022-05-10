import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# The following test is based on the observation that
# gc.collect() will not collect objects that are only
# reachable via a weak reference.  The test creates a
# circular reference and a weak reference to one of the
# objects in the cycle.  It then forces a collection and
# verifies that the referenced object is still alive.
# It then breaks the reference and verifies that the
# object has been collected.

class C:
    pass

c = C()
wr = weakref.ref(c)
c.x = c

gc.collect()

if wr() is not None:
    print "test_gc failed"

c = None

gc.collect()

if wr() is not None:
    print "test_gc failed"

print "test_gc passed"
