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

# The weakref to LateFin should be dead now, and the weakref to func
# should have been cleared.  But the LateFin instance should still
# exist, and its __del__ method should call func().  This should
# succeed, since the func object is still alive.
del latefin
gc.collect()

print("OK")
