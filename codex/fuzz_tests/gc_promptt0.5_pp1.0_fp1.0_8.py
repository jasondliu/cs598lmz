import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a callback
# This test is a bit tricky because we have to make sure
# the callback doesn't keep the object alive.

# Create a callback that keeps a reference to the object
# and a list to store the callback in.
results = []
def callback(obj):
    results.append(weakref.ref(obj))

# Create a list of objects to be collected
objs = [object(), object(), object(), object()]

# Register the callback
gc.callbacks.append(callback)

# Collect the objects
gc.collect()

# Make sure the callback was called
assert len(results) == 4
assert results[0]() is objs[0]
assert results[1]() is objs[1]
assert results[2]() is objs[2]
assert results[3]() is objs[3]

# Make sure the callback didn't keep the objects alive
results = []
gc.collect()
assert len(results) == 0
 
# Test gc.collect() with a callback that raises an exception
# This test is a bit tricky because we have
