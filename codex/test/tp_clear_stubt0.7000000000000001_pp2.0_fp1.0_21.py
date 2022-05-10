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

print(gc.collect())
print(gc.collect())

# LateFin has a reference to a dead object
gc.garbage.append(latefin)

# the dead object has a reference to the LateFin instance
gc.garbage.append(latefin.ref)

# the LateFin instance has a ref to func
print(gc.collect())
# del latefin, func

# the dead object has a reference to the LateFin instance
gc.garbage.append(latefin.ref)

# the LateFin instance has a ref to func
print(gc.collect())
