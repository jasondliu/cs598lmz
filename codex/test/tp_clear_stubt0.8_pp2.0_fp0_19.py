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
# We overwrite func in module with the new, random object --
# it should be cleaned due to module cleanup
# (not a bug in this test -- it doesn't matter whether the object
# is cleaned or not, but it will be seen as a refleak if it isn't)
del latefin
gc.collect()

# We now overwrite func again with a new, random object -- it should be
# cleaned due to module cleanup.
func = lambda: None
func.__module__ = 'abc'
gc.collect()
