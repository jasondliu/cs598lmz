import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# This test is to make sure that gc.collect() works in the face
# of weakrefs to objects that are part of a reference cycle.

# Create a reference cycle.
class C:
    pass

c1 = C()
c2 = C()
c1.other = c2
c2.other = c1

# Create a weakref to one of the objects in the cycle.
w = weakref.ref(c1)

# Break the cycle.
c1 = None
c2 = None

# Make sure the weakref is still alive.
if w() is None:
    raise TestFailed("weakref died prematurely")

# Trigger a full collection.
gc.collect()

# Make sure the weakref is still alive.
if w() is None:
    raise TestFailed("weakref died prematurely")

# Create a reference cycle.
class C:
    pass

c1 = C()
c2 = C()
c1.other = c2
c2.other = c1

# Create a weakref to one of the objects
