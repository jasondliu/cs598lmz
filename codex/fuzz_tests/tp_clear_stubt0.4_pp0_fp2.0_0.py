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

# the next line should raise an AttributeError, but it doesn't
# because the __del__ method of the Cyclic class is called
# before the LateFin class, and the __del__ method of the
# LateFin class is called after the __del__ method of the
# Cyclic class.
print(latefin.ref())
