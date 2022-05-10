import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class Test:
    pass
# Create two objects
obj1,obj2 = Test(), Test()
# Collect between creation of first and second object.
# This should make the first object collectable.
gc.collect()
assert gc.collectable(obj1)
# Collect again.
# This should make the first object uncollectable again.
gc.collect()
assert not gc.collectable(obj1)
# Create a cycle to the first object.
obj2.ref = obj1
# Now both objects should be collectable.
gc.collect()
assert gc.collectable(obj1)
assert gc.collectable(obj2)
# Finally break the cycle.
obj2.ref = None
# Now only the second object should be collectable.
gc.collect()
assert not gc.collectable(obj1)
assert gc.collectable(obj2)
# Clear references to both objects.
obj1 = None
obj2 = None
gc.collect()
