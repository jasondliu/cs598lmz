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
#print(latefin.ref)
#print(latefin.ref())

# This is evil.  The weakref object is kept alive by the LateFin object,
#  and since LateFin is in the same module as the weakref, the module
#  can't be freed.  If the weakref is in another module, the module is
#  freed.  If we use a function instead of a lambda, the module goes away
#  too.

# This test is disabled for now.  We should fix the bug anyways.
#  It shouldn't be too hard to fix.
#assert latefin.ref() is None
