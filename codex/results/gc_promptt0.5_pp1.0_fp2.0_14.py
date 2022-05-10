import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after a weakref callback
# (This is a regression test for SF bug #424720)

# Create a cyclic structure
class C:
    pass
c = C()
c.c = c

# Create a weakref to it with a callback
wr = weakref.ref(c, lambda x: None)

# Delete the cyclic structure
del c

# Run the garbage collector
gc.collect()

# Check that the weakref is still alive
if wr() is not None:
    print "Weakref is still alive"
else:
    raise RuntimeError
