import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C(object):
    pass

# The list of objects to be collected is weakly referenced.
# Now, a list can only be garbage collected when it is empty,
# so we need a list with a finalizer.
class D(object):
    def __init__(self):
        self.x = []
    def __del__(self):
        pass

def test_basic_collect(n):
    print 'test_basic_collect(%d)' % n
    gc.collect()
    gc.collect()
    gc.collect()
    gc.collect()
    for i in xrange(n):
        c = C()
        d = C()
        c.x = d
        d.x = c
    gc.collect()
    gc.collect()
    gc.collect()
    gc.collect()

def test_list_collect():
    print 'test_list_collect()'
    gc.collect()
    gc.collect()
    gc.collect()
    gc.collect()
   
