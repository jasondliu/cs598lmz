import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(...)
class B(object):
    pass

# A collection of objects to be tested.
b0 = B()
b1 = B()
b2 = B()
b3 = B()
b4 = B()
b5 = B()
b6 = B()
b7 = B()
b8 = B()
b9 = B()

# A dict used to keep track of which objects are alive.
live = {
    'b0': b0,
    'b1': b1,
    'b2': b2,
    'b3': b3,
    'b4': b4,
    'b5': b5,
    'b6': b6,
    'b7': b7,
    'b8': b8,
    'b9': b9,
}

# Set up the circular references
b0.ref = b1
b1.ref = b2
b2.ref = b3
b3.ref = b4
b4.ref = b5
b5.ref = b6
b6.ref =
