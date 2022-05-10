import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback
# This tests the fix for bug #829604

# Create a callback that will be called when the weakref is
# about to be collected.  It will append the id of the object
# to a list.

# Create a class with a __del__ method that will be called
# when the instance is collected.  It will append the id of
# the instance to a list.

class C:
    def __init__(self, id):
        self.id = id
    def __del__(self):
        self.id = None
        del self.id

# Create a list of weak references to objects, and a list of
# objects with __del__ methods.

wlist = []
dlist = []

# Create a bunch of objects, and arrange for the weakref callback
# to be called when the weakref to the object is about to be
# collected.  Also arrange for the __del__ method to be called
# when the object is about to be collected.

for i in range(100):
    o = C(i)
    dlist
