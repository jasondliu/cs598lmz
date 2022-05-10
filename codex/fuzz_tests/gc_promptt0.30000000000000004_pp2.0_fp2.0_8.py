import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable objects.
# This test is a bit tricky:  it creates a cycle with a list object
# at its center.  The cycle also contains a dict, so that the list
# has a length and can't be merged with other lists.  The list also
# has a finalizer, so that it's kept alive by the finalizer mechanism.
# The cycle is broken when the finalizer runs.

# Create the list object at the center of the cycle.
l = []
l.append(l)
l.append({})

# Create a finalizer that will break the cycle when the list is collected.
def finalize(ref):
    l = ref()
    del l[0]

# Create a weak reference to the list.
weak = weakref.ref(l, finalize)

# Collect everything.
gc.collect()

# Verify that the list is now gone.
assert weak() is None, "list wasn't collected"

# Verify that the list was collected.
gc.collect()
assert gc.garbage == [], "list wasn't collected"

# Create
