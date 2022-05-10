import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(x):
    print "callback", x

def test():
    f = Foo()
    r = weakref.ref(f, callback)
    print "callback should not be called yet"
    del f
    print "callback should be called now"
    gc.collect()
    print "callback should not be called again"

test()
