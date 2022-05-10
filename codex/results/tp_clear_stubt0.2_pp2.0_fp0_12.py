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
gc.collect()

# This is a bit tricky.  The LateFin object is not yet finalized,
# but the weakref callback has been called.  The callback sets the
# func variable to the weakref of the LateFin object.  The LateFin
# object is finalized, and the func variable is set to None.  The
# func variable is then deleted, and the LateFin object is
# finalized.  The LateFin object is finalized, and the func variable
# is set to None.  The func variable is then deleted, and the LateFin
# object is finalized.  The LateFin object is finalized, and the
# func variable is set to None.  The func variable is then deleted,
# and the LateFin object is finalized.  The LateFin object is
# finalized, and the func variable is set to None.  The func variable
# is then deleted, and the LateFin object is finalized.  The LateFin
# object is finalized, and the func variable is set to None.  The
# func variable is then deleted, and the LateFin object is
# finalized.  The LateFin object
