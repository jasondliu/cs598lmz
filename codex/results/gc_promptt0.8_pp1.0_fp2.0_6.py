import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() invokes tp_clear on reachable objects
# for which tp_clear is defined.

# This is a bit of an arbitrary example.  In real life,
# I think most types that define tp_clear are also defined
# with tp_traverse, but that doesn't matter for gc.collect().

import weakref
import gc

class C:
    pass

class D:
    pass

class E(int):
    def __new__(cls, *args, **kwds):
        x = int.__new__(cls, *args, **kwds)
        x.wr = weakref.ref(x)
        return x
    def __init__(self, *args, **kwds):
        print "E.__init__", self, self.wr() is self
        C.__init__(self)
    def __del__(self):
        print "E.__del__", self, self.wr()
        C.__del__(self)

class F(E, C, D):
    pass


