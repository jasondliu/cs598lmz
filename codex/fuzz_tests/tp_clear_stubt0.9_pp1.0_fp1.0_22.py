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

# Check that func has been deleted indirectly by the __del__
# of latefin
gc.collect()

# Exercise the dictionary updating code: we replace the value
# of func with a callable function while the key is alive.

class DelOnCalled:
    def __call__(self):
        global fin1
        del fin1

fin1 = DelOnCalled()
cyclic = {}
cyclic[cyclic] = cyclic

cyclic[0] = fin1
cyclic[1] = fin1
finalizer = CycFinalizer(cyclic, cyclic)

del fin1
del cyclic

# Exercise the finalization of a weakref referencing an object
# from its __del__ implemented in Python.

class DelRefToSelf:
    def __del__(self):
        global fin2
        del fin2
        global x
        x.weakref = weakref.ref(self)

x = DelRefToSelf()
fin2 = x
del x
gc.collect()

# Test finalizers for which
