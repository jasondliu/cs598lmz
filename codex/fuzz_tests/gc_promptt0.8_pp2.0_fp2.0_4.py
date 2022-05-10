import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
#
# Create a reference cycle.
class Foo:
    pass

x = Foo()
x.x = x

# Now queue x for collection.
ref = weakref.ref(x)
del x
x = None

# Demonstrate that the reference cannot be accessed.
assert ref() is None

# Demonstrate that the cycle is collectable (x is a ghost).
assert gc.collectable(ref)

# Demonstrate that the cycle is no longer collectable.
assert not gc.collectable(ref)
