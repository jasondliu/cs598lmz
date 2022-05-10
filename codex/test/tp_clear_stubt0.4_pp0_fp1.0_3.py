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

# now we have a function with a __del__, and a LateFin instance with a
# __del__ that's still alive.  The LateFin instance has a reference to
# the function, so the function's __del__ won't run.  But the LateFin
# instance's __del__ will run, and it will set func to None.  So the
# function should be freed, and the LateFin instance should be freed
# too.

gc.collect()

# if we're still here, then the function and LateFin instances are both
# still alive.  That's bad.

import sys
print(sys.getrefcount(func))
print(sys.getrefcount(latefin))

