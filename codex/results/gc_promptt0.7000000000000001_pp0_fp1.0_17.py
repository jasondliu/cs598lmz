import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage with weakly reachable objects.
#
# [XX] The test currently only checks that gc.garbage is non-empty,
# i.e. that some objects were collected.  It should check that the
# collected objects are the ones we expect.

# In a debug build, gc.collect() may free twice as many objects as it
# normally would.  If gc_collect_count is set, it's the number of
# objects the test expects gc.collect() to collect.
gc_collect_count = 0

# A list of objects that should be garbage-collected.
garbage = []

class A:
    pass

# Make a cycle that is only weakly reachable
a = A()
b = A()
a.x = b
b.x = a

garbage.append(a)
weakref.ref(b)

# Make a cycle that is only weakly reachable, and contains a __del__
class B:
    def __del__(self):
        pass
b = B()
b.x =
