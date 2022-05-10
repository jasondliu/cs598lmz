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

# Exercise the code that is executed when a module is deleted.
# This is a separate test because the code is not exercised by
# the above test.

import sys

class M:
    __slots__ = ('__dict__',)

m = M()
m.__dict__ = m
sys.modules['m'] = m
del m
