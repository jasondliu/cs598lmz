import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# Create a bunch of objects, and make sure they are all collected.
#
# This test is a bit tricky, because we want to make sure that
# gc.collect() collects *everything* that is collectable, but we don't
# want to depend on *how* the collector happens to collect things.
# For example, we can't assume that the collector will find every
# reachable object via reachability from the GC root, because the
# collector isn't required to use such an algorithm.  So we arrange
# for a bunch of stuff to be reachable, and then we try collect, and
# make sure a whole bunch of stuff disappears, and some specific stuff
# we've arranged to be collectable does get collected.

# Create a bunch of old-style classes, and instances of those classes,
# and make sure they are all collected.

class C1:
    pass
class C2:
    pass
class C3:
    pass
class C4:
    pass
class C5:
    pass
class C6:
    pass
class C7:
    pass
class C8
