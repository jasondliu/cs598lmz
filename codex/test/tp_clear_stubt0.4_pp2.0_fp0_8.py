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

# This is the real test:  if the function object is not collected,
# the weakref will be cleared, and the LateFin object will not be
# collected.  If the function object is collected, the LateFin
# object will be collected, and the weakref will not be cleared.
# The next line will raise an exception if the weakref is not
# cleared.
del latefin.ref

# This is just a sanity check.  It will raise an exception if the
# function object is not collected.
del func
