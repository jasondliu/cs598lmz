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

# This testcase is checking that the following sequence of events
# does not happen:
#
# - cyclic garbage is collected by a full collection
# - cyclic garbage is finalized
# - the finalizer for the cyclic garbage assigns to a global (latefin)
# - the global is finalized
# - the finalizer for the global calls a function (func)
# - the function is finalized
# - the function's module (the cyclic garbage) is finalized
# - the finalizer for the module tries to call the function
#
# This is an ordering problem; the standard CPython implementation
# will not run into this problem, but other python implementations
# may run into it.
