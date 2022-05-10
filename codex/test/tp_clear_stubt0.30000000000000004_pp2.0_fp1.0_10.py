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

# The following line will cause a crash if the bug is present.
# It will also cause a crash if the bug is fixed, but the fix
# is incomplete (e.g. if the fix only works for functions
# defined in the module __main__).
print(latefin.ref())
