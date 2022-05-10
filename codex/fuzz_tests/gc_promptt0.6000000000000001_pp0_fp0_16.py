import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a weakref
class A:
    pass

a = A()
wr = weakref.ref(a)
a = None
gc.collect()
print wr()
print wr() is None
