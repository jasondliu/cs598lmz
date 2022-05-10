import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(wr):
    print "callback", wr

def test():
    f = Foo()
    wr = weakref.ref(f, callback)
    print wr
    del f
    gc.collect()
    print wr

test()
