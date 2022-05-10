import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs and weakref callbacks.

# Test that gc.collect() calls the callbacks of weakrefs whose referents
# are unreachable.

# This test checks that gc.collect() calls the callbacks of weakrefs
# whose referents are unreachable.

# Create a class with a __del__ method.
class A:
    def __del__(self):
        print("A.__del__")
        # Create a new A object.
        self.other = A()

# Create a weakref to an A object.
a = A()
r = weakref.ref(a)

# Create a cycle involving a.
a.other = a

# Break the cycle.
a = None

# Collect garbage.
gc.collect()

# Check that the weakref callback was called.
if r() is not None:
    print("weakref callback not called")

# Check that the second A object was collected.
gc.collect()
if gc.collect() != 0:
    print("second A object not collected")


