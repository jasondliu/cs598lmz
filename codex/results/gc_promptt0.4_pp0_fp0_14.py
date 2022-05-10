import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is a bit tricky, because gc.collect() doesn't return the
# number of objects collected.  We have to use a side channel to
# determine that.

# Create a bunch of objects, and determine how many are still alive
# after a collect.

# We have to use a list of weak references, because if we use a
# dictionary, the dictionary itself will keep the objects alive.

# Create a bunch of objects.
objects = [C() for i in range(10)]

# Create a bunch of weak references to the objects.
refs = [weakref.ref(obj) for obj in objects]

# Create a bunch of cycles.
objects += [[obj] for obj in objects]

# Create a bunch of cycles involving old-style classes.
objects.append(C())
objects[-1].attr = objects[-1]

# Create a bunch of cycles involving new-style classes.
objects.append(D())
objects[-1].attr = objects[-1]

# Create a bunch of cycles involving instances of built-in types.
objects.
