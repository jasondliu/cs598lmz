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

# collect the function and the tuple.  The function
# must not be collected yet (in the C versions, that
# would call __del__ twice, causing a segfault)
gc.collect()

# now the function should be collected, calling __del__
# twice, the second time with a NULL unbound method.
gc.collect()
