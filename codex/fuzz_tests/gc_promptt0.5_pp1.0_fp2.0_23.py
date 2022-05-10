import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with cyclic trash and __del__
#
# This test checks that gc.collect() works when there are objects
# involved in reference cycles that have __del__ methods.

import gc, weakref

class C:
    def __init__(self):
        self.x = C()

    def __del__(self):
        print "deleting", self

c = C()

# Create a reference cycle.
c.x.x = c

# Test that gc.collect() can break the cycle.
gc.collect()

# Create a second reference cycle.
c.x.x = c

# Make sure that the second reference cycle is detected.
gc.collect()

# Create a reference cycle with a __del__ method.
c = C()
c.x.x = c

# Test that gc.collect() can break the cycle.
gc.collect()

# Create a second reference cycle.
c.x.x = c

# Make sure that the second reference cycle is detected.
gc.collect()

# Test that gc.
