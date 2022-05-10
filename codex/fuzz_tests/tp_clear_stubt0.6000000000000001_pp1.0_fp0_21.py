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

class Cyclic2:
    __slots__ = ('__weakref__', 'ref')
    def __del__(self):
        self.ref = weakref.ref(self)
        global latefin
        del latefin

cyc = Cyclic2()
cyc.__module__ = cyc
del cyc
gc.collect()

# Verify that we can call the function after the cyclic finalizers have
# run.
assert func() is None
