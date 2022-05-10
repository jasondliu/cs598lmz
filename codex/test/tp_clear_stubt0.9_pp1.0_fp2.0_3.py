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
gc.collect()
gc.collect()

"""
Important is that objA__del__() is longer than objB__del__(), otherwise
it may happen that objB gets deleted, thus the weakref in objA remains
alive, thus objA will never be deleted.

The cyclic reference alone is not enough, it must be introduced at a point
later than where the weakref is destroyed.
"""
