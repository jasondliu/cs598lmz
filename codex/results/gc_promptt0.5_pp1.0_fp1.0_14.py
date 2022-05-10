import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test was written to test the fix for SF bug #478577.

import gc

# Create a reference cycle.
class A:
    pass

a = A()
a.b = A()
a.b.a = a

# Check that the objects are tracked by the GC.
assert gc.is_tracked(a)
assert gc.is_tracked(a.b)

# Check that the objects are in gc.garbage.
gc.collect()
assert a in gc.garbage
assert a.b in gc.garbage

# Check that the objects are still tracked by the GC.
assert gc.is_tracked(a)
assert gc.is_tracked(a.b)

# Check that the objects are still in gc.garbage.
gc.collect()
assert a in gc.garbage
assert a.b in gc.garbage

# Delete references to the objects.
del a
del a.b

# Check that the objects are still tracked by the GC.
assert
