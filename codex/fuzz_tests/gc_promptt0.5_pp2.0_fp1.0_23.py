import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when we have a weakref to an object with a __del__
# method that creates a reference cycle.
#
# This test is designed to fail when run with Python versions before 2.3.
# It passes with 2.3 and 2.4a0.

# Create a reference cycle.
class C:
    def __init__(self):
        self.x = []
    def __del__(self):
        self.x.append(self)

c = C()

# Create a weak reference to c.
w = weakref.ref(c)

# Delete c, and verify that it still exists.
del c
gc.collect()
assert w() is not None

# Create a reference cycle including c.
l = [w]

# Delete c's last reference, and verify that it still exists.
del l
gc.collect()
assert w() is not None

# Delete the weak reference, and verify that c is destroyed.
del w
gc.collect()
assert gc.collect() == 0
