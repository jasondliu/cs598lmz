import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# This class does not define an __init__, __del__ method or
# have any __slots__.  It is therefore very amenable to weakrefs.
class C:
    pass

# Create a cycle.
c = C()
d = C()
c.foo = d
d.foo = c

# Create a weak reference to d
w = weakref.ref(d)

# Collect and verify that d is still live.
gc.collect()
if w() is None:
    raise TestFailed, 'd was collected wrongly'

# Try deallocating d...
del d

# ...and collect again.  d shouldn't be collected now.
gc.collect()
if w() is None:
    raise TestFailed, 'd was collected wrongly'

# Break the cycle
c.foo = None

# ...and collect again.  d should be collected now.
gc.collect()
if w() is not None:
    raise TestFailed, 'd was not collected'

# Now recreate the cycle, and make sure it doesn't get collected

