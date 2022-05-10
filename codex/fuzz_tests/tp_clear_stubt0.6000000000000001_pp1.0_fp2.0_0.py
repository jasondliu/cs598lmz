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
del func, cyc, LateFin, Cyclic

gc.collect()

try:
    del latefin.ref
except AttributeError:
    pass
else:
    raise Exception("shouldn't be able to del latefin.ref")

print("before del latefin")
del latefin
print("after del latefin")

gc.collect()

del func

gc.collect()

print("OK")
