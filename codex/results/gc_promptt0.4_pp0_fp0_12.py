import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    pass

def callback(wr):
    print "callback", wr, wr()

def test():
    f = Foo()
    c = weakref.ref(f, callback)
    print "c", c, c()
    del f
    gc.collect()
    print "c", c, c()
    f = Foo()
    c = weakref.ref(f, callback)
    print "c", c, c()
    del f
    gc.collect()
    print "c", c, c()
    f = Foo()
    c = weakref.ref(f, callback)
    print "c", c, c()
    del f
    gc.collect()
    print "c", c, c()
    f = Foo()
    c = weakref.ref(f, callback)
    print "c", c, c()
    del f
    gc.collect()
    print "c", c, c()
    f = Foo()
    c = weakref.ref(f
