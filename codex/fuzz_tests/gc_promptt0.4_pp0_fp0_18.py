import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

def callback(w):
    print 'callback', w()

def test():
    a = A()
    w = weakref.ref(a, callback)
    print 'before', w()
    del a
    gc.collect()
    print 'after', w()

test()
