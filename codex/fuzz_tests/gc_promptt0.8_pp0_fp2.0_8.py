import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect bit...
ob = weakref.proxy(TestClass())

# ... now we know that gc.collect will collect stuff
gc.collect()

# and that gc.DEBUG_COLLECTABLE works
assert gc.collect() == 1
assert gc.collect() == 0

# Check that gc.DEBUG_OBJECTS works
# First, trace all object creation
assert gc.get_debug() == 0
gc.set_debug(gc.DEBUG_OBJECTS)
ob = TestClass()
assert gc.get_count() == 2

# We know the next 2 lines will not collect, so the count won't decrease
ob = TestClass()
assert gc.get_count() == 2
del ob
assert gc.get_count() == 2

# Now test the count with a collection
assert gc.collect() == 1
assert gc.get_count() == 1

# And that gc.DEBUG_UNCOLLECTABLE works
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
ob = TestClass()
ob.ob = ob
