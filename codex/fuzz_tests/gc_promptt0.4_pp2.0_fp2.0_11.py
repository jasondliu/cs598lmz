import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to an object that has a __del__ method.
# This used to fail because the object was not collectable.

class A:
    def __del__(self):
        pass

a = A()
wr = weakref.ref(a)
del a
gc.collect()
print wr() is None
