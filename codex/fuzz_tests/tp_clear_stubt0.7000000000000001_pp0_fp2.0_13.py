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
del func, cyc, LateFin

gc.collect()
gc.collect()
gc.collect()
gc.collect()

assert latefin.ref is None

# Because latefin.ref is None, the first attempt to call func() will fail
# and set func to None.  The second attempt to call func() should then
# raise a TypeError.

try:
    func()
except TypeError:
    pass
try:
    func()
except TypeError:
    pass

# Check that the weakref was not deallocated too early
assert latefin.ref is None

del func, latefin
gc.collect()
gc.collect()
gc.collect()
gc.collect()
