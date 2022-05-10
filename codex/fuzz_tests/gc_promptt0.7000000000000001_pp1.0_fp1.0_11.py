import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect destruction of weakrefs to instance.
# Verify that weakrefs to objects that are collected are also removed.
import sys
import gc
import weakref

class X(object):
    pass

x = X()
ref = weakref.ref(x)

# Verify that the weakref gets cleared when the object is deleted.
del x
gc.collect()
assert ref() is None

# Verify that the weakref gets cleared when the object is deleted
# after the weakref is cleared.
class Y:
    pass
y = Y()
ref = weakref.ref(y)
del y
del ref
gc.collect()

# Verify that the weakref gets cleared when the object is deleted
# after the weakref is cleared.
class Z(object):
    def __del__(self):
        pass
z = Z()
ref = weakref.ref(z)
del z
del ref
gc.collect()

# Verify that the weakref gets cleared when the object is deleted
# after the weakref is cleared.
class A(object):
    def __del__(self):
