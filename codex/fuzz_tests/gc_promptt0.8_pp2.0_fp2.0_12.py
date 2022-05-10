import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() as an example of a function that
# uses tp_traverse.
#
print 'gc.collect()...'
gc.collect()
print 'done.'
#
# This should raise ValueError:
#
print 'gc.collect(2)...'
gc.collect(2)
print 'done.'
#
# The following code illustrates a weakness in the current
# cyclic gc: if a container is part of a cycle, but nobody
# else points to any of the objects in the container, they
# will be collected, leaving the container in an
# inconsistent state.  This was considered a risk worth
# taking: in most (all?) real-life cases, the other objects
# also are part of cycles, so will not be collected.  It's
# only conceivable pathological cases like this one where
# the problem could show up.
#
# BTW, this is the reason why there's no UNCOLLECTABLE flag
# in the GC HEAD flags (there used to be one before the
# tri-color algorithm was implemented).
#
class C:
    def __init__(self, n):
       
