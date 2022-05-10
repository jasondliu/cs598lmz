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

if latefin.ref is None:
    print('SKIP')
    raise SystemExit

# Create a new function with the same name, but in a different module.
func = lambda: None

# The old func is dead now, but we can't collect it because of the cyc
# object.  It is safe to collect it now.
del latefin
gc.collect()

# This should crash because the old func is dead.
func()
