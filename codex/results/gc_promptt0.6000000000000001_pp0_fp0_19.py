import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after a weakref callback deletes the last reference to an
# object.

def callback(ignored):
    print "callback"

def test():
    gc.collect()
    r = weakref.ref(gc.collect, callback)
    gc.collect()
    del r
    gc.collect()

test()
