import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() bug when there is a weakref for an old-style class
# with a finalizer

class A:
    pass

def fin():
    pass

# Create an old-style class with a custom finalizer
A.__del__ = fin

a = A()
wr = weakref.ref(a)
gc.collect()
del a
gc.collect()
print wr()
