import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage.
# Note that gc.garbage can be empty even if gc.collect() frees some
# objects.  This is because the objects may be freed without being
# put on gc.garbage, and because gc.garbage is cleared before
# gc.collect() is called.

# Create a bunch of objects, and record the set of all objects
# reachable from the global namespace.
all = {}
for name, value in globals().items():
    all[id(value)] = 1

# Create a cycle, and verify that it is found.
o = C()
o.cycle = o
del o
gc.collect()
if gc.garbage:
    print(gc.garbage)
    raise TestFailed('gc.garbage not empty')

# Create a reachable object that looks like it's part of a cycle, but
# really isn't.  This tests the "visit" routine in gcmodule.c.
o = C()
o.cycle = o
del o
gc.collect()
if gc.gar
