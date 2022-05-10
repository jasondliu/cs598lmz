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
del func, cyc, latefin
gc.collect()

# This used to segfault.  It now raises a ReferenceError, which is
# correct.  (The segfault was caused by the fact that the module
# object was freed before the function object, so the function
# object's tp_clear handler tried to clear func.__module__, which
# had already been freed.)
