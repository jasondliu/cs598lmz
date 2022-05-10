import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before and after the weakref callback is invoked.
def callback(r):
    gc.collect()
    print 'callback'

class C:
    pass

def test():
    gc.collect()
    r = weakref.ref(C(), callback)
    gc.collect()

test()
