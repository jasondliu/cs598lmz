import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when a cyclic trash can contains objects
# with __del__ methods

class A:
    def __del__(self):
        pass

class B(A):
    def __init__(self, a):
        self.a = a

a = A()
b = B(a)
a.b = b
del b, a

import gc
gc.collect()

# Verify that all objects in the trashcan are now (or soon will be)
# unreachable.
gc.collect()

# If a __del__ method is run and adds a trash object to a cyclic trash can,
# check that the resulting layout is handled correctly.

class A:
    def __del__(self):
        self.b = B(self)

class B(A):
    def __init__(self, a):
        self.a = a

a = A()
a.b = B(a)
del a

import gc
gc.collect()

# The trashcan layout for this test is a diamond if the unreachable
# objects are all in
