import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when a weakref is created
# during the collection of a finalizer.
#
# This is a test for a bug in 3.2, where the
# finalizer-object would be collected, but the
# weakref to it would remain.
#
# The bug was that the weakref would be added
# to the list of objects to be notified, but
# the weakref itself would not be marked as
# reachable.
class Dummy:
    pass

class C:
    def __del__(self):
        o = Dummy()
        o.x = self
        wr = weakref.ref(o)

c = C()
c.x = C()
c.x.y = c
del c
gc.collect()
