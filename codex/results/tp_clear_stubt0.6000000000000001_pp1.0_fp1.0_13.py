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

# no crash (latefin is now a dead reference)

# the above is a hack to get the following test to work
# in a way that doesn't crash.  The test is:

import weakref

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic((lambda: None, Cyclic
