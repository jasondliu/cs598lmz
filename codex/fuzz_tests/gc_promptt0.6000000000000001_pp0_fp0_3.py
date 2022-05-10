import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after an object has been finalized.
from test import test_support

class A:
    pass

class B(A):
    pass

# Create a cycle, so the objects can't be freed.
a = A()
b = B()
a.b = b
b.a = a

# Delete the references.
del a, b

# The objects are still alive, because they're part of a cycle.
gc.collect()

# Break the cycle.
B.__del__ = lambda self: self.a.b = None

# The objects can now be freed.
gc.collect()

# Check that a new collection will free the objects.
gc.collect()

# Create a new cycle.
a = A()
b = B()
a.b = b
b.a = a

# Delete the references.
del a, b

# The objects are still alive, because they're part of a cycle.
gc.collect()

# Break the cycle.
B.__del__ = lambda self: None

# The objects can now be freed.
gc
