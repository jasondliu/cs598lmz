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
gc.collect()  # Create a late-deleting object.

# Create a cyclic reference to it,
# which will be cleared when the cyclic reference is broken.
latefin.ref = weakref.ref(latefin)
del latefin

# The cyclic reference is broken, but the late-deleting object remains.
gc.collect()

# The weakref is cleared, and the late-deleting object is deleted.
gc.collect()
</code>

