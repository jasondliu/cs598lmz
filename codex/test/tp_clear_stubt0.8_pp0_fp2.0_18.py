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

# Since the weakref callback has a cyclic reference to the instance,
# it will prevent cpython from freeing the instance's memory slot.
# But pypy will free the memory slot, because it stores weakrefs
# that are used by a weakref callback in a separate array.
gc.collect()
