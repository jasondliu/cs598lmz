import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# This test is to make sure that collect() works even when there are
# weakrefs to unreachable objects.  The problem was that the unreachable
# objects were not moved to the head of the freelist, so the weakref
# objects were not cleared.

class MyObject(object):
    pass

def callback(wr):
    print "callback", wr

def test():
    obj = MyObject()
    wr = weakref.ref(obj, callback)
    obj2 = MyObject()
    obj2.obj = obj
    del obj
    del obj2
    gc.collect()
    print wr()

test()
