import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.

# Create a bunch of objects.
objects = [object() for i in range(10)]

# Create a bunch of weak references to them.
refs = [weakref.ref(obj) for obj in objects]

# Delete the objects.
del objects

# Trigger a collection.
gc.collect()

# Check that the weak references still exist.
for r in refs:
    assert r() is not None

# Check that the objects don't exist.
for obj in gc.get_objects():
    for r in refs:
        if obj is r():
            break
    else:
        assert 0, "object still alive"

# Create a bunch of objects.
objects = [object() for i in range(10)]

# Create a bunch of weak references to them.
refs = [weakref.ref(obj) for obj in objects]

# Delete the objects.
del objects

# Trigger a collection.
gc.collect()

# Check that the weak references still exist.
for r in refs:
    assert r()
