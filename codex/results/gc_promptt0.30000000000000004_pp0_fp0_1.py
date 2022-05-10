import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback
# This should not crash

class A:
    pass

def callback(x):
    print 'callback'

a = A()
wr = weakref.ref(a, callback)
del a
gc.collect()
print 'done'
