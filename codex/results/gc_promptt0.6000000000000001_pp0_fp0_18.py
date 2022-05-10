import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to a tuple.
#
# This test is not intended to be run in a production environment
# because it changes the garbage collection thresholds.

# Set the garbage collection thresholds to (1, 2).
gc.set_threshold(1, 2, 2)

# Create a tuple.
t = (1, 2, 3)

# Create a weak reference to the tuple.
w = weakref.ref(t)

# Create a cycle with the tuple at its root.
t = t,

# Invoke gc.collect() and check the weak reference.
collected = gc.collect()
assert collected == 0
assert w() is not None

# Invoke gc.collect() and check the weak reference.
collected = gc.collect()
assert collected == 1
assert w() is None
