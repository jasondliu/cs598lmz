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

for i in range(50):
    gc.collect()

del LateFin.__del__
assert not hasattr(latefin, 'ref')
del LateFin.__del__

sys.getrefcount(latefin)  # Clear the refcount cache

del latefin
gc.collect()
del LateFin.__del__

print("passed all tests")
