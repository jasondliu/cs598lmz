import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        A.__init__(self)
        self.y = 2

def callback(obj):
    print "callback", obj
    print gc.get_referrers(obj)

a = A()
a.b = B()
a.b.a = a
a.b.b = a.b
a.b.c = weakref.ref(a.b, callback)

gc.collect()
del a
gc.collect()
print gc.garbage
print "end"
