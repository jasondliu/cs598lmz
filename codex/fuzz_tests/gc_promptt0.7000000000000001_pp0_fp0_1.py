import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs in various states.

class C(object):
    pass

# Create an instance.
c = C()

# Create a weakref to the instance.
w = weakref.ref(c)

# The weakref and object point to each other,
# and the object is collectable.
assert gc.collect() == 1

# The weakref is not dead, and the object is still alive.
assert w() is c

# Break the cycle.
del c

# The object is now collectable.
assert gc.collect() == 1

# The weakref is dead, and the object is still alive.
assert w() is None

# The object is not collectable.
assert gc.collect() == 0

# The weakref is still dead, and the object is still alive.
assert w() is None

# Create a new instance.
c = C()

# Create another weakref to the new instance.
w = weakref.ref(c)

# The weakref and object point to each other,
# and the object is collectable
