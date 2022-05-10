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
del func, cyc, latefin
gc.collect()
print(len(gc.garbage))
gc.garbage.clear()
print(len(gc.garbage))

##      0
##      0

"""
Python 3.2
==========

Cycle is detected and cleared, so the object has no references left.
(Note that Py3.2 and Py3.3 differ in the implementation of this;
in Py3.2 the cycle is detected at the tuple side, in Py3.3 it's
detected at the LateFin side; in both cases we print 0).
"""

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
cyc = tuple.__new
