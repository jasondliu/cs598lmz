import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect of cycles like in issue https://bugs.python.org/issue13678
# where collectable objects have a finalizer whose cyclic trash caused gc to
# ignore the object.
class C:
    def __init__(self,x):
        self.x = x
        self.wr = weakref.ref(self)
    def __del__(self):
        pass

o = C(100)
o.self = o

sys.getrefcount(o)
del o
gc.collect()
# test weakref basic operation
import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# test __eq__ and __hash__
wr0 = weakref.ref(3)
wr1 = weakref.ref(3)
wr2 = weakref.ref(4)
wr3 = weakref.ref(3)
wr4 = wr1
wr5 = wr2
# "note that neither refs() nor vals() calls __hash__() or __eq__() of referent objects"
wr1() is wr0()
wr1() ==
