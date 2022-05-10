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

# now we have a weakref pointing to a function object, and the function
# object's __module__ points to the weakref.  The weakref is in a
# cycle, and the function object is in a cycle.  The weakref is
# reachable from the function object, and the function object is
# reachable from the weakref.  The cycle is not collectable.

# If we break the cycles, the weakref and the function object should
# get collected.

latefin = None
gc.collect()
gc.collect()

# If the test passes, the function object has been collected.  If the
# test fails, the function object has not been collected, and we'll
# get a RuntimeError when we try to call it.
func()
