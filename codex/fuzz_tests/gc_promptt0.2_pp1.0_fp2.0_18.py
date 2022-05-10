import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def callback(w):
    print "callback called"

def test():
    f = Foo()
    wr = weakref.ref(f, callback)
    print wr()
    del f
    gc.collect()
    print wr()

test()

# Test gc.garbage

def test():
    f = Foo()
    wr = weakref.ref(f, callback)
    print wr()
    del f
    gc.collect()
    print wr()
    print gc.garbage

test()
