import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

class A:
    pass

class B:
    pass

class C:
    pass

def callback(w):
    print "callback"
    gc.collect()
    print "callback done"

a = A()
b = B()
c = C()

a.b = b
b.a = a

a.c = c
c.a = a

w = weakref.ref(a, callback)

del a, b, c

print "collecting"
gc.collect()
print "collecting done"
