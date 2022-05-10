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

try:
    del latefin.ref
except AttributeError:
    pass
else:
    raise TestFailed("__del__ called on a weakref proxy that's still valid")

try:
    del latefin.__module__
except AttributeError:
    raise TestFailed("__del__ not called on a weakref proxy that's no longer valid")
</code>

