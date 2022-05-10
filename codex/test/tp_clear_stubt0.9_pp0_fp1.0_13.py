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

del latefin

###########################################################################

# Make sure that a weakref to a new-style class cleans up the referent.

class X(object):
    __slots__ = ('a',)

    def __init__(self):
        self.a = 2

w = weakref.ref(X())

