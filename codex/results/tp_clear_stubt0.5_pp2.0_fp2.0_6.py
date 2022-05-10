import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()

# the next line triggers the bug: the cyclic reference
# between the function and the LateFin object is not
# detected, and the LateFin object is not cleared.
# This causes the weakref callback to be called with a
# dangling pointer.
del latefin
gc.collect()

# The bug is that the function object is not cleared,
# because it is reachable from its module.  The module
# is not cleared because it is reachable from the
# LateFin object.  The LateFin object is not cleared
# because it is reachable from the weakref callback.
# The weakref callback is not cleared because it is
# reachable from the LateFin object.
#
# The weakref callback should be cleared!
