import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback on a collectable object.
# This also used to test gc.get_referrers(), but get_referrers() has
# been disabled because it is too expensive.

class A:
    pass

def callback(wr):
    print "callback", wr()

def make_callback(x):
    return callback

a = A()
wr = weakref.ref(a, callback)

# make the object collectable
del a
gc.collect()

a = A()
wr = weakref.ref(a, make_callback(a))

del a
gc.collect()

class X:
    def __del__(self):
        print "X.__del__"

x = X()
wr = weakref.ref(x, callback)

del x
gc.collect()
