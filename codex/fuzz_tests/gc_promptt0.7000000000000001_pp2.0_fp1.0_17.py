import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A(object):
    def __del__(self):
        print 'deleting', self

def test_collect():
    class B(object):
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return "B(" + self.name + ")"
        def __del__(self):
            print "deleting", self
    #
    # Create and collect a bunch of cycles of different lengths.
    # The length of the cycle doesn't affect collection, but this
    # used to crash Python 2.1, so let's test it.
    #
    for i in range(5):
        for j in range(i):
            a = B("a" + str(i))
            b = B("b" + str(i))
            a.x = b
            b.x = a
        #
        # The exact number of objects collected should be (i+1)*2,
        # but Python only guarantees that at least that many objects
        # will be collected.  The number of objects actually
