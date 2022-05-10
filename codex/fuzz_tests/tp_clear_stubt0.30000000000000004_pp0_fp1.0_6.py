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

# This is a bit of a hack.  We need to make sure that the
# LateFin object is not collected before the Cyclic object.
# The easiest way to do that is to make sure that the
# LateFin object is reachable from the Cyclic object.
# We do that by making the LateFin object a weakref.ref
# to itself.  The LateFin object is then reachable from
# the Cyclic object, and the Cyclic object is reachable
# from the LateFin object.
latefin.ref = weakref.ref(latefin)

del latefin
gc.collect()

# The LateFin object should now be gone, and the func
# object should be a weakref.ref to None.  We need to
# make sure that the func object is not collected before
# we can call it.  We do that by making it a global.
func()
