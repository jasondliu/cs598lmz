import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

class A:
    pass

def callback(wr):
    print "callback"

a = A()
wr = weakref.ref(a, callback)

gc.collect()

del a
gc.collect()

print wr()

gc.collect()

print wr()
