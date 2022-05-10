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

# Check that the cyclic reference was broken
# This test is not very reliable, but it is a best-effort
# It is not possible to reliably detect whether the cyclic reference
# was broken, because the __del__ methods are not guaranteed to run
# (and in fact, when running with -O, they won't run)
if latefin.ref() is not None:
    print("Error: cyclic reference not broken")
else:
    print("OK")
