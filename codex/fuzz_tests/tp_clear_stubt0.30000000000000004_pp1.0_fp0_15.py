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

# This is the important part.  We need to make sure that the
# LateFin object is not finalized before the Cyclic object.
# If it is, then the weakref callback will be called, and
# the function will be finalized.  If the function is finalized
# before the Cyclic object, then the weakref callback will not
# be called, and the test will pass.
#
# The test is to make sure that the LateFin object is not finalized
# before the Cyclic object.  If it is, then the weakref callback
# will be called, and the function will be finalized.  If the
# function is finalized before the Cyclic object, then the weakref
# callback will not be called, and the test will pass.
#
# The test is to make sure that the LateFin object is not finalized
# before the Cyclic object.  If it is, then the weakref callback
# will be called, and the function will be finalized.  If the
# function is finalized before the Cyclic object, then the weakref
# callback will not be called, and the test will pass
