import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def callback(x):
    print "callback called"

def test():
    f = Foo()
    w = weakref.ref(f, callback)
    del f
    print gc.collect()
    print w()

test()
