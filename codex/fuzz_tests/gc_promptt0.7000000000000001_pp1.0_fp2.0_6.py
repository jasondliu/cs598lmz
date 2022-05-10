import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with collectable objects
#
# This tests the collect() function with objects that are collectable.
#
# If you see "gc_collect: collectable <XXX>", then the object can be
# collected.  If you see "gc_collect: uncollectable <XXX>", then the
# object can't be collected.
#
# This test will fail if the Python interpreter has been built without
# cyclic gc support, because it creates cyclic gc objects.
#
# This test is a bit tricky.  It creates a bunch of objects, and then
# stores weak references to half of them.  If everything is working
# correctly, the objects without weak references should be collected,
# but the objects with weak references should not be collected.

import gc

class A:
    pass

# Create a bunch of objects, and store weak references to half of them.
al = [A() for i in range(100)]
wl = [weakref.ref(al[i]) for i in range(0, len(al), 2)]
# Clear the strong references
del al
# Collect
gc.
