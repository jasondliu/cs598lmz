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

weakref.proxy(latefin)

# https://bugs.python.org/issue35926
# Avoid a segfault when a weakref to a finalizer is garbage collected
# using a custom __del__

import gc, weakref

class Cyclic:
    __slots__ = ()
    def __del__(self):
        self.ref = weakref.ref(self)
        global latefin
        del latefin

latefin = Cyclic()
cyc = Cyclic()
cyc.ref = weakref.ref(cyc)

gc.collect()

weakref.proxy(latefin)

# https://bugs.python.org/issue36046
# Avoid a segfault when a weakref to a finalizer is garbage collected
# using a custom __del__ calling a weakref.proxy

import gc, weakref

class Cyclic:
    __slots__ = ()
    def __del__(self):
        self.ref = weakref.ref(self)
        global latefin
       
