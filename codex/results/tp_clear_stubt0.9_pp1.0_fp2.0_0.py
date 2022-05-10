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
collect()
gc.garbage.append(latefin)

del gc.garbage[:]
collect()
del latefin
collect()
import sys; print >>sys.stderr, gc.garbage
import gc; assert not gc.garbage, gc.garbage

unmodified = pass
