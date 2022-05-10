import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C(object):
    def __init__(self, a):
        self.a = a
    def __del__(self):
        print "del"

def test_collect():
    gc.collect()
    c = C(1)
    gc.collect()
    c = None
    gc.collect()
    c = C(1)
    gc.collect()
    c = C(1)
    gc.collect()
    c = C(1)
    gc.collect()
    c = None
    gc.collect()
    c = C(1)
    gc.collect()
    c = C(1)
    gc.collect()
    c = C(1)
    gc.collect()
    c = C(1)
    gc.collect()
    c = C(1)
    gc.collect()
    c = C(1)
    gc.collect()
    c = C(1)
    gc.collect()
    c = C(1)
    gc
