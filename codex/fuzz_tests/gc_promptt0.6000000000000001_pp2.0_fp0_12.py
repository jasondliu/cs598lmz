import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before creating weakrefs
gc.collect()

# Create weak references to all objects and store them in a list
objs = []
for o in gc.get_objects():
    objs.append(weakref.ref(o))

# Clear references to the objects
del gc.garbage[:]
del objs

# Test gc.collect()
gc.collect()

# Check whether it works
gc.collect()
print len(gc.garbage)

# Create weak references to all objects and store them in a list
objs = []
for o in gc.get_objects():
    objs.append(weakref.ref(o))

# Clear references to the objects
del gc.garbage[:]
del objs

# Test gc.collect()
gc.collect()
