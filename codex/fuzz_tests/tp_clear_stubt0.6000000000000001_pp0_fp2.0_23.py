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
del func, cyc, latefin
gc.collect()

# This is a rather unusual way to get a __del__ method called,
# but it's the easiest way to avoid having any other objects
# in the cycle.

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

import gc
gc.collect()
