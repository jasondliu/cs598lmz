import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a dangling cycle.
# This can fail (incorrectly) with early versions of Python 2.4.
class A(object):
    pass
a = A()
wr = weakref.ref(a)
del a
gc.collect()
print wr()
