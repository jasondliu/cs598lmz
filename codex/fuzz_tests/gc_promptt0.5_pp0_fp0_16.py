import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

class A:
    def __del__(self):
        print "A.__del__"

def callback(wr):
    print "callback", wr

a = A()
w = weakref.ref(a, callback)
print w
del a
print w
gc.collect()
print w
