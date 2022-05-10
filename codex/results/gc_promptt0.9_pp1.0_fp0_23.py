import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect when there is a bug in collection.

# Create some cycles in __del__ functions.
class X:
    def __del__(self):
        self.y = Y()

class Y:
    def __del__(self):
        self.x = X()

x = []
for i in range(20):
    x.append(X())

gc.collect()
gc.garbage[1].__del__()

class Z:
    def __del__(self):
        x = []
        x.append(x)

z1 = Z()
z2 = Z()

z1wr = weakref.ref(z1)
z2wr = weakref.ref(z2)

del z1
del z2

gc.collect()

# To clear the problem described in sourceforge bug #494016,
# an __del__ method must be able to rely on the simple assumption
# that the __del__ method is being called because the reference count
# reached zero.
#
# This code relies on an ordering of GC.  We guarantee that a
