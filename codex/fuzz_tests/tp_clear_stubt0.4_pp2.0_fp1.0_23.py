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
gc.collect()
del latefin

# Verify that the late-deleting object is still alive, and that
# the weakref is still alive.
assert gc.collect() == 0
assert gc.collect() == 0
assert gc.collect() == 0

print('ok')
