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

# The following line is expected to fail with a RuntimeError
# (because the function object was deleted).
#
# If it doesn't, then the bug is not present.
#
# If it does, then the bug is present, but it is not guaranteed
# that the test has detected it.

latefin.ref()

# The following line is expected to fail with a RuntimeError
# (because the weakref object was deleted).
#
# If it doesn't, then the bug is not present.
#
# If it does, then the bug is present, but it is not guaranteed
# that the test has detected it.

del latefin
gc.collect()
