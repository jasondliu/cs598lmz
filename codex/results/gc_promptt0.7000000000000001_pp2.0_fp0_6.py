import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref.
# It should not collect anything until the weak references are invalidated.

class Dummy:
    pass

class Dummy2:
    pass

def callback(w):
    print "callback"
    del w

d = Dummy()
d2 = Dummy2()

del d
d = weakref.ref(d2, callback)

gc.collect()

del d2
gc.collect()
