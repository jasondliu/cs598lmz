import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

class A:
    pass

def callback(w):
    print 'callback', w

a = A()
w = weakref.ref(a, callback)
del a
gc.collect()
print 'done'
