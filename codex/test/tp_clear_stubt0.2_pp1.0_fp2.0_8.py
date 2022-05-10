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

# Check that the cyclic reference is broken
assert latefin.ref() is None

# Check that the function is still alive
assert latefin.ref is not None

# Check that the function is still callable
assert latefin.ref()() is None

# Check that the function is still alive
assert latefin.ref is not None

# Check that the function is still callable
assert latefin.ref()() is None

# Check that the function is still alive
assert latefin.ref is not None

# Check that the function is still callable
assert latefin.ref()() is None

# Check that the function is still alive
assert latefin.ref is not None

# Check that the function is still callable
assert latefin.ref()() is None

# Check that the function is still alive
assert latefin.ref is not None

# Check that the function is still callable
assert latefin.ref()() is None

# Check that the function is still alive
assert latefin.ref is not None

# Check that the function is still call
