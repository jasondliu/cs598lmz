import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

class A:
    pass

class B:
    pass

def callback(wr):
    print "callback"

a = A()
b = B()
a.b = b
b.a = a

a_wr = weakref.ref(a, callback)
b_wr = weakref.ref(b, callback)

del a
del b

gc.collect()

print "done"
