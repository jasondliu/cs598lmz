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

# This is a regression test for a bug in the garbage collector.
# The bug was that the garbage collector didn't call tp_clear()
# on objects that were part of a reference cycle, but that
# contained a __del__ method.  This caused the weakref
# in the __del__ method to not be cleared, and thus caused
# a memory leak.
#
# The bug was originally found by running the Python test suite
# under Purify, and was fixed by adding the 'visit_decref' function
# to gcmodule.c.  The test case here was written by Tim Peters.

import gc

class C:
    def __init__(self, n):
        self.n = n
    def __del__(self):
        pass

class D:
    def __init__(self, n):
        self.n = n
    def __del__(self):
        pass

class E:
    def __init__(self, n):
        self.n = n
    def __del__(self):
        pass
