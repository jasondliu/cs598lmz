import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without a generational collector.
gc.disable()

# Create a list of objects.  Use a list so we can easily iterate over
# them later without creating references to them.
objects = [object() for i in range(10)]

# Create some weakrefs to them.
refs = [weakref.ref(obj) for obj in objects]

# Enter some of the objects in the circular garbage.
objects[1].other = objects[2]
objects[2].other = objects[3]
objects[3].other = objects[1]

# Delete all references to the objects.
del objects

# Collect garbage.  This used to crash, but no longer does.
gc.collect()

# Check the weakrefs.  The first two should be dead, the rest live.
if len(list(filter(lambda r: r() is not None, refs))) != 8:
    raise RuntimeError("wrong number of weak references remain alive")
