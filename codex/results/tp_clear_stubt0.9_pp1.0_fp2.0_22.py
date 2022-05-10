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

# Because Python currently ignores __del__ methods when references on gcable
# objects are still alive and the __del__ method invokes the gc, it may not
# be possible, or take a long time, to reproduce this crash.
if (latefin.ref, None) != (None, None):
    latefin.ref().__class__.x.__doc__ = 'a'
