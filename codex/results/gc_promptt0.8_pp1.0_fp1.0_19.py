import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def check():
    gc.collect()
    gc.collect()
    # Should be no collectable objects
    assert gc.collect() == 0
# A test class
class Test:
    pass
# Create a reference to a Test object
t = Test()
# Get a reference to it
r = weakref.ref(t)
# Remove the local reference
t = None
check()
# Make sure it wasn't collected
assert r() is not None
# Collect again
gc.collect()
# Make sure it was collected
assert r() is None
