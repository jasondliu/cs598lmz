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

# This is the interesting part:
# - func is a function object, which has a reference to its module
# - latefin is a LateFin object, which has a reference to func
# - cyc is a Cyclic object, which has a reference to both func and latefin
# - func.__module__ is a reference to cyc
# - latefin.ref is a weakref to func
# - cyc[1].ref is a weakref to cyc[0]
#
# The interesting part is that when cyc is deleted, it will delete
# latefin, which will call func, which will set latefin.ref to None.
# This will cause func to be deleted, which will delete cyc[0], which
# will delete cyc, which will delete latefin, which will call func,
# which will set latefin.ref to None.  This will cause func to be
# deleted, which will delete cyc[0], which will delete cyc, which will
# delete latefin, which will call func, which will set latefin.ref to
# None.  This will
