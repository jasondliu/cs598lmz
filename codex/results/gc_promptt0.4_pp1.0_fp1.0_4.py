import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.

# Create a list of objects to be collected.  Use a list to make sure
# they are all found by gc.collect().

objects = []

# Create a bunch of weakrefs to the objects.  The weakrefs are
# created first so they are found by gc.collect() before the objects
# are.

refs = []

for i in range(1000):
    o = C()
    objects.append(o)
    refs.append(weakref.ref(o))

# Collect the objects.  This should also collect the weakrefs.

gc.collect()

# Check that all the objects were collected, and all the weakrefs
# point to dead objects.

for i in range(len(objects)):
    if objects[i] is not None:
        print "object", i, "not collected"
    if refs[i]() is not None:
        print "weakref", i, "not collected"

# Create a bunch of weakrefs to the objects.  The weakrefs are

