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
del func, cyc, LateFin, Cyclic
gc.collect()
del latefin
gc.collect()

# ____________________________________________________________
#
#  Test for bug #1405877:  a crash when the finalizer for a weakref
#  calls a method of the referent after the referent has been deleted.
#  The crash occurs in the tp_dealloc handler for the weakref.

class C:
    def __del__(self):
        self.x = 42

class D:
    def __init__(self):
        self.ref = weakref.ref(C())
    def __del__(self):
        self.ref().x

D()
gc.collect()

# ____________________________________________________________
#
#  Test for bug #1405879:  a crash when a finalizer for a weakref
#  calls a method of the referent that raises an exception.

class C:
    def __del__(self):
        raise TypeError

class D:
    def __init__(self):
        self.ref = weakref.ref(C())
