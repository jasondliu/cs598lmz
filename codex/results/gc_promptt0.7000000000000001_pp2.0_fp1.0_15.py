import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable
#
# gc_collectable() is only useful for debugging, not in real code.
# gc_collectable() returns true if the object is only referenced from
# the garbage collector and can be collected when the next collection
# takes place.

# Create an object which is not garbage collected, and test it
class Dummy: pass
o = Dummy()
del Dummy
print(gc.collectable(o))
o = Dummy()
del Dummy
print(gc.collectable(o))
# Create an object which is not garbage collected, and test it
class Dummy: pass
o = Dummy()
del Dummy
print(gc.collectable(o))
o = Dummy()
del Dummy
print(gc.collectable(o))
# Create an object which is not garbage collected, and test it
class Dummy: pass
o = Dummy()
del Dummy
print(gc.collectable(o))
o = Dummy()
del Dummy
print(gc.collectable(o))
# Create an object which is not garbage collected, and test it
class D
