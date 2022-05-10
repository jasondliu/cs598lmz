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

# This should not crash.  If it does, then the __del__ method in
# Cyclic was called before the __del__ method in LateFin.  This
# would be a bug, because LateFin's __del__ method needs to run
# first in order to set the 'func' global.
assert latefin.ref() is None
